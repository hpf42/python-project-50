.PHONY: clean install package-install build gendiff lint test check


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


check: test lint


gendiff:
	uv run gendiff