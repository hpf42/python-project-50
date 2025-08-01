.PHONY: clean install package-install build gendiff parser 


clean:
	rm -rf dist/ build/ *.egg-info


install:
	uv sync


package-install: build
	uv tool install dist/*.whl


build:
	uv build


gendiff:
	# uv run gendiff/scripts/gendiff.py
	# uv run gendiff
	# uv run python3 -m gendiff.scripts.gendiff
	uv run python3 -m gendiff.scripts.gendiff #file1.json file2.json


parser:
	uv run python3 -m gendiff.scripts.parser


lint:
	uv run ruff check gendiff


test:
	uv run pytest


check: test lint