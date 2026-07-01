from __future__ import annotations

from .ensemble import ModelEnsemble
from .tool import ModelTool

RegistryItem = ModelTool | ModelEnsemble


class ToolRegistry:
    """Bundles multiple ModelTools (and optional ModelEnsembles) for bulk export."""

    def __init__(
        self,
        tools: list[ModelTool],
        ensembles: list[ModelEnsemble] | None = None,
    ) -> None:
        names = [t.name for t in tools] + [e.name for e in (ensembles or [])]
        duplicates = sorted({name for name in names if names.count(name) > 1})
        if duplicates:
            raise ValueError(f"Duplicate tool or ensemble names are not allowed: {duplicates}.")
        self._tools: dict[str, ModelTool] = {t.name: t for t in tools}
        self._ensembles: dict[str, ModelEnsemble] = {e.name: e for e in (ensembles or [])}

    def get(self, name: str) -> RegistryItem:
        if name in self._tools:
            return self._tools[name]
        if name in self._ensembles:
            return self._ensembles[name]
        available = list(self._tools) + list(self._ensembles)
        raise KeyError(f"No tool or ensemble named '{name}'. Available: {available}")

    def to_openai(self) -> list[dict]:
        return [t.to_openai() for t in self._tools.values()] + [
            e.to_openai() for e in self._ensembles.values()
        ]

    def to_langchain(self) -> list:
        return [t.to_langchain() for t in self._tools.values()] + [
            e.to_langchain() for e in self._ensembles.values()
        ]
