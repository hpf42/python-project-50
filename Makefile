.PHONY: clean install build gendiff package-install


clean:
	rm -rf dist/ build/ *.egg-info

install:
	uv sync

package-install:
	uv tool install dist/*.whl

build:
	uv build

gendiff:
	# uv run gendiff/scripts/gendiff.py
	uv run gendiff

