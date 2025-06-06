# Suggested Shell Commands for link-kicker Project

## Package Management (uv)
- `uv sync` - Install/update dependencies from uv.lock
- `uv add <package>` - Add new dependency
- `uv remove <package>` - Remove dependency
- `uv run <command>` - Run command in project environment
- `uv pip list` - List installed packages

## Development Workflow
- `make run` - Start the bot (equivalent to `uv run python -m main`)
- `make lint` - Run black and isort code formatting
- `make black` - Run black code formatter only
- `make isort` - Run isort import sorter only

## Database Operations
- `uv run aerich upgrade` - Apply database migrations
- `uv run aerich migrate` - Create new migration
- `uv run aerich downgrade` - Rollback migrations

## Locale Management
- `sh scripts/compile_locales.sh` - Compile locale files (.po → .mo)
- `sh scripts/extract_update_locales.sh` - Extract/update translatable strings

## Testing Environment
- `uv run python -c "import app.config"` - Test app imports
- `uv run python --version` - Check Python version in environment

## Docker (if needed)
- `docker-compose up` - Start services (Redis, PostgreSQL, etc.)
- `docker-compose down` - Stop services

## Git Operations
- Standard git commands apply
- Current branch: poetry-to-uv (migration branch)
- Main branch: master

## Safety Notes
- NEVER run destructive commands like `rm -rf`
- Always test imports after dependency changes
- Use `uv sync` instead of manual pip installs