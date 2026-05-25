from __future__ import annotations
from typing import Any, Callable

import numpy as np
from pydantic import BaseModel

from .introspect import introspect
from .coerce import coerce_inputs
from .exporters.openai import to_openai_schema
from .exporters.langchain import to_langchain_tool


class ModelTool:
    """Wraps a fitted sklearn-compatible model as an LLM-callable tool."""

    def __init__(
        self,
        model: Any,
        name: str,
        description: str,
        input_schema: type[BaseModel],
        output_name: str,
        output_description: str,
    ) -> None:
        self.model = model
        self.name = name
        self.description = description
        self.input_schema = input_schema
        self.output_name = output_name
        self.output_description = output_description
        self._meta = introspect(model)

    def invoke(self, input_dict: dict) -> dict:
        """Validate inputs, run prediction, return {output_name: value}."""
        try:
            validated = self.input_schema(**input_dict)
        except Exception as exc:
            raise ValueError(f"Input validation failed for '{self.name}': {exc}") from exc

        features = coerce_inputs(validated, self._meta)
        X = self._to_array(features)
        prediction = self.model.predict(X)[0]

        if hasattr(prediction, "item"):
            prediction = prediction.item()

        return {self.output_name: prediction}

    def to_openai(self) -> dict:
        """Return an OpenAI function-calling schema dict."""
        return to_openai_schema(self)

    def to_langchain(self):
        """Return a LangChain StructuredTool."""
        return to_langchain_tool(self)

    def to_callable(self) -> Callable[..., dict]:
        """Return a plain Python function that calls invoke()."""
        def _fn(**kwargs) -> dict:
            return self.invoke(kwargs)
        _fn.__name__ = self.name
        _fn.__doc__ = self.description
        return _fn

    def _to_array(self, features: list) -> Any:
        feature_names = self._meta.get("feature_names")
        if feature_names:
            try:
                import pandas as pd
                return pd.DataFrame([dict(zip(feature_names, features))])
            except ImportError:
                pass
        return np.array([features])
