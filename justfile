# Django-Todolist — task runner
# Requires: https://github.com/casey/just

set dotenv-load := false

[private]
default:
    @just --list

# Run the full local CI gate
check:
    just lint
    just format-check
    just deps
    just django-check
    just migration-check
    just test

# Run the test suite
test:
    uv run python manage.py test

# Run Ruff's linter
lint:
    uv run ruff check .

# Auto-fix lint and formatting issues
fix:
    uv run ruff check --fix .
    uv run ruff format .

# Check formatting without modifying files
format-check:
    uv run ruff format --check .

# Check declared dependencies
deps:
    uv run deptry .

# Run Django's system checks
django-check:
    uv run python manage.py check

# Verify that model changes have migrations
migration-check:
    uv run python manage.py makemigrations --check --dry-run

# Upgrade all dependencies and sync the environment
update:
    uv lock --upgrade
    uv sync
