.PHONY: lint typecheck test

lint:
	uv run ruff check --fix src

typecheck:
	uv run mypy

test:
	uv run pytest --cov=src --cov-report=xml
