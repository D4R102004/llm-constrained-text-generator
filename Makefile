.PHONY: install lint format test run clean

install:
	pip install -e ".[dev]"
	pre-commit install
	pre-commit install --hook-type commit-msg

lint:
	ruff check src/ tests/

format:
	ruff format src/ tests/

test:
	pytest

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name .pytest_cache -exec rm -rf {} +
	find . -type d -name .ruff_cache -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name ".coverage" -delete

run:
	python -m ai_project.interface
