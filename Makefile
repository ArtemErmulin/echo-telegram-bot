check-linters:
	uv run black --check ./src
	uv run isort --check-only ./src
	uv run autoflake --check --recursive ./src

fix-linters:
	uv run black ./src
	uv run isort ./src
	uv run autoflake --in-place --recursive ./src
