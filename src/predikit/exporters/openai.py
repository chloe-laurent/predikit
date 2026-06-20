from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..ensemble import ModelEnsemble
    from ..tool import ModelTool


def to_openai_schema(tool: ModelTool | ModelEnsemble) -> dict:
    """Convert a ModelTool to an OpenAI function-calling schema dict."""
    schema = tool.input_schema.model_json_schema().copy()
    schema.pop("title", None)

    return {
        "type": "function",
        "function": {
            "name": tool.name,
            "description": tool.description,
            "parameters": schema,
        },
    }
