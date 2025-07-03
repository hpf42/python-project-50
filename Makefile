.PHONY: clean install build gendiff


clean:
	rm -rf dist/ build/ *.egg-info

install:
	uv sync

build:
	uv build

gendiff:
	uv run gendiff/scripts/gendiff.py


