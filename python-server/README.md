# python-server

## Setup

```bash
uv sync --all-groups
cp .env.example .env
```

## Commands

```bash
make lint        # ruff check + fix
make typecheck   # mypy
make test        # pytest with coverage
```

## Project structure

```
src/
├── __init__.py
├── settings.py          # pydantic-settings config from .env
├── app/                 # entrypoint — CLI (typer) or API (fastapi)
│   ├── __init__.py
│   └── main.py
├── models/              # pydantic models / domain types
│   └── __init__.py
├── services/            # business logic
│   └── __init__.py
├── clients/             # external API / DB clients
│   └── __init__.py
└── utils/               # shared helpers (logging, etc.)
    └── __init__.py
tests/
├── __init__.py
├── test_*.py
└── conftest.py          # shared fixtures
```

Create only the folders you need — not all projects require every layer.
