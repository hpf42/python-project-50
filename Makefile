.PHONY: clean install package-install build gendiff lint test check test-coverage


clean:
	rm -rf dist/ build/ *.egg-info


install:
	uv sync


package-install: build
	uv tool install dist/*.whl


build:
	uv build


lint:
	uv run ruff check gendiff


test:
	uv run pytest


test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml:coverage.xml


check: test lint


gendiff:
	uv run gendiff