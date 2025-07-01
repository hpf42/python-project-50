clean:
	rm -rf dist/ build/ *.egg-info

install:
	uv sync

build:
	uv build

gendiff:
	uv run gendiff