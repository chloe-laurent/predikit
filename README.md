# modelbridge
Opensource contribution

# modelbridge — v0.1 Build Spec

**One-line pitch:** Turn any trained sklearn/XGBoost model into an LLM-callable tool with auto-generated schemas and typed I/O. Framework-agnostic.

**Problem it solves:** LLM agents can call functions, but wrapping ML models as agent tools means hand-writing JSON schemas, input validators, and output formatters every time. `modelbridge` does this automatically from the model's own metadata.

---

## What it does (in 4 steps)

1. **Wrap** — User passes a fitted model + a Pydantic input schema + a name/description to `ModelTool(...)`.
2. **Introspect** — Library auto-extracts feature names, output type, and class labels from the model.
3. **Export** — User calls `.to_openai()` or `.to_langchain()` to get a tool definition usable by any agent framework.
4. **Invoke** — When the LLM calls the tool, `modelbridge` validates/coerces inputs, runs `.predict()`, and returns a typed dict.

---

## Core API surface (memorize this)

```python
ModelTool(
    model,                # fitted sklearn-compatible estimator
    name: str,            # tool name the LLM sees
    description: str,     # tool description the LLM sees
    input_schema,         # Pydantic BaseModel describing inputs
    output_name: str,     # key for the prediction in returned dict
    output_description: str,
)

ModelTool methods:
    .invoke(input_dict) -> dict          # validates, coerces, predicts
    .to_openai() -> dict                 # OpenAI function-calling schema
    .to_langchain() -> Tool              # LangChain Tool object
    .to_callable() -> Callable           # plain typed Python function

ToolRegistry([tool1, tool2, ...])
    .to_openai() -> list[dict]
    .to_langchain() -> list[Tool]
    .get(name) -> ModelTool
```

That's the entire public API. Five methods on `ModelTool`, three on `ToolRegistry`. Don't add more for v0.1.

---

## Folder structure

```
modelbridge/
├── pyproject.toml
├── README.md, LICENSE (MIT), .gitignore
├── .github/workflows/{test.yml, publish.yml}
├── src/modelbridge/
│   ├── __init__.py       # exports ModelTool, ToolRegistry
│   ├── tool.py           # ModelTool class
│   ├── registry.py       # ToolRegistry class
│   ├── introspect.py     # extract metadata from sklearn models
│   ├── coerce.py         # type coercion (str→float, etc.)
│   └── exporters/{openai.py, langchain.py}
├── tests/                # pytest, one file per module
└── examples/
    ├── 01_basic_sklearn.py
    ├── 02_xgboost_regression.py
    └── 03_orlando_real_estate.py    # your portfolio demo
```

---

## v0.1 scope — IN

- [x] `ModelTool` wraps sklearn-compatible models (anything with `.predict` / `.predict_proba`)
- [x] Auto-introspection: `feature_names_in_`, `classes_`, output dtype
- [x] Pydantic input schemas with basic type coercion (str→int/float, bool parsing)
- [x] Exporters: OpenAI function-calling JSON, LangChain Tool, plain callable
- [x] `ToolRegistry` for bundling multiple tools
- [x] Helpful errors when LLM hands you malformed inputs
- [x] Tests on Python 3.10, 3.11, 3.12
- [x] Working Orlando example

## v0.1 scope — OUT (roadmap, mention in README)

- [ ] Confidence-aware routing & fallback
- [ ] Multi-model synthesis (agent calls several, reconciles)
- [ ] MLflow / Snowflake Model Registry integration
- [ ] HuggingFace / PyTorch / TensorFlow support
- [ ] Async invocation
- [ ] Streaming outputs

---

## Build order (do in this sequence)

1. **Check PyPI name availability** — visit `pypi.org/project/modelbridge/`. First 404 wins.
2. **Write the README** — design forced through docs. If the README isn't compelling, the API isn't right.
3. **Stub `tool.py`** — signatures + docstrings, no implementation. Make sure it *reads* well.
4. **Implement `introspect.py`** — pure function: model → metadata dict. Easy to test in isolation.
5. **Implement `coerce.py`** — pure function: (value, target_type) → coerced value. Easy to test.
6. **Implement `ModelTool.invoke()`** — ties introspect + coerce + predict together.
7. **Implement exporters** — straightforward translations of metadata into framework formats.
8. **Implement `ToolRegistry`** — thin wrapper, mostly delegation.
9. **Write the Orlando example** — the README's hero demo. Must actually run.
10. **Publish to TestPyPI first**, then real PyPI.

---

## Definition of done for v0.1

- `pip install modelbridge` works
- README has a 30-second code example that runs as written
- Orlando example in `examples/` runs end-to-end
- ≥70% test coverage on `src/modelbridge/`
- GitHub Actions runs tests on every PR
- LinkedIn announcement post drafted

---

## Anti-scope (things that will tempt you — say no)

- Don't add an agent runtime. You wrap models; users bring their own agent loop.
- Don't add model training helpers. You're a tooling library, not a modeling library.
- Don't add a CLI. v0.1 is a Python API only.
- Don't support every sklearn estimator edge case. Get the 80% case clean; document gaps.
- Don't make it async. Sync is fine for v0.1.
