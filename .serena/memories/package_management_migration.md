# Package Management Migration: Poetry → uv

## Project Status
- **Successfully migrated** from Poetry to uv package management
- **Migration date**: January 2025
- **Python version**: 3.9+ (currently using 3.9.12)

## Current Dependencies (Pinned Versions)
- aiogram==2.22.1 (Telegram bot framework)
- tortoise-orm[asyncpg]==0.17.8 (ORM with PostgreSQL support)
- loguru==0.5.3 (Logging)
- aerich==0.5.8 (Database migrations for Tortoise ORM)
- celery==5.1.2 (Task queue)
- redis==3.5.3 (Redis client)
- aioredis==1.3.1 (Async Redis client)
- PyYAML>=6.0 (YAML parser - upgraded from 5.4.1 due to build issues)
- And other dependencies...

## Package Management Commands
- **Install dependencies**: `uv sync`
- **Run commands**: `uv run <command>`
- **Add new dependency**: `uv add <package>`
- **Remove dependency**: `uv remove <package>`

## Build Configuration
- **Build system**: hatchling (replaced poetry-core)
- **Package structure**: `app/` directory contains the main package
- **Lock file**: `uv.lock` (replaced poetry.lock)

## Development Workflow
- **Run bot**: `make run` (uses `uv run python -m main`)
- **Linting**: `make lint` (runs black and isort via uv)
- **Migrations**: `uv run aerich upgrade`
- **Locale compilation**: `sh scripts/compile_locales.sh`

## Important Notes
- Dependencies are pinned to exact versions from the original poetry.lock to maintain compatibility
- The project uses very old library versions (2021-2022 era) - future updates may require handling breaking changes
- aiogram v2 is EOL - consider upgrading to v3 in the future (breaking changes expected)
- aioredis v1 is old - v2+ has breaking changes