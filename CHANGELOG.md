# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.4.4] - 2026-06-24

### Changed
- README overhauled: added "Why predikit?" comparison table, "Works with" ecosystem section, GitHub star/fork badges, and a shipped-vs-planned roadmap
- Quick start section replaces "30-second example" heading; `---` dividers added between major sections for better scanability
- PyPI package description updated to a more descriptive one-liner
- Keywords expanded: added `scikit-learn`, `tool-use`, `openai`, `langchain`, `mlops`, `ai-agents`, `pydantic`, `model-serving`
- Added `Documentation` URL to `[project.urls]` in `pyproject.toml`
- Added `Topic :: Software Development :: Libraries :: Python Modules` and `Typing :: Typed` classifiers

## [0.4.2] - 2026-06-13

### Changed
- Redesigned PyPI/README hero: logo, centered tagline, and badges in a unified `<p align="center">` block
- Tagline moved from a `##` heading to a proper descriptive paragraph
- Badges converted to centered HTML `<img>` links for consistent rendering on PyPI
- Quick code teaser repositioned directly below badges (before Table of Contents)
- "Field naming rule" added to Table of Contents
- `ainvoke()` added to `ModelTool` Core API reference table
- `ModelEnsemble` Core API subsection added with constructor signature and full strategy table
- Project Traffic / download badge moved to bottom of README
- Development Status classifier bumped from `3 - Alpha` to `4 - Beta` in `pyproject.toml`
- Removed CI test status badge from README

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
