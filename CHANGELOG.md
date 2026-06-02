# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.4.1] - 2026-06-02

### Added
- `ruff` (lint + format) and `mypy` (type checking) configured in `pyproject.toml`
- `.pre-commit-config.yaml` — ruff and mypy hooks run automatically before every commit
- Lint CI job in GitHub Actions — runs `ruff check`, `ruff format --check`, and `mypy` on every push and PR
- `CONTRIBUTING.md` — development setup, code style, and PR guidelines
- `CHANGELOG.md`
- `CLAUDE.md` — project context for Claude Code

### Changed
- Bumped version to `0.4.1`
- Added `ruff>=0.4.0`, `mypy>=1.10`, and `pre-commit>=3.0` to `[dev]` extras

## [0.4.0] - 2026-05-01

### Added
- `ModelEnsemble` with `weighted_mean` and `weighted_vote` strategies
- `ainvoke()` async wrapper on `ModelTool` (runs blocking predict in a thread pool)
- Verbose logging via `verbose=True` on `ModelTool`
- Snowflake Model Registry loader (`from_snowflake`)
- MLflow Model Registry loader (`from_mlflow`)
- `predikit inspect` CLI command

### Changed
- Moved to `src/` layout with hatchling build backend
- Upgraded Pydantic dependency to v2

## [0.3.x] and earlier

See [GitHub Releases](https://github.com/Tejas-TA/predikit/releases) for earlier history.
