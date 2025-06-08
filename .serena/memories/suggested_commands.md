# Suggested Development Commands

## Essential Commands for Development

### Package Management
- `uv sync` - Install/update dependencies from uv.lock
- `uv add <package>` - Add a new dependency
- `uv add --group dev <package>` - Add a development dependency
- `uv remove <package>` - Remove a dependency

### Code Quality
- `make lint` - Run ruff check and format (recommended before commits)
- `make check` - Check code with ruff linter
- `make format` - Format code with ruff
- `make check-fix` - Check and auto-fix code with ruff
- `uv run ruff check .` - Alternative way to run ruff check
- `uv run ruff format .` - Alternative way to run ruff format

### Database Operations
- `uv run aerich upgrade` - Apply database migrations
- `uv run aerich migrate` - Generate new migrations from model changes
- `uv run aerich init-db` - Initialize database schema

### Internationalization
- `sh scripts/extract_update_locales.sh` - Extract and update translation files
- `sh scripts/compile_locales.sh` - Compile locale files (required before running)

### Running the Application
- `make run` - Start the bot (equivalent to `uv run python -m main`)
- `uv run python -m main` - Alternative way to start the bot

### Development Services
- `docker-compose up -d` - Start PostgreSQL and Redis services
- `docker-compose down` - Stop services

### System Commands (macOS)
- `ls` - List directory contents
- `find` - Search for files
- `grep` - Search text in files  
- `git` - Version control operations

## Workflow
1. Start services: `docker-compose up -d`
2. Install dependencies: `uv sync`
3. Apply migrations: `uv run aerich upgrade`
4. Compile locales: `sh scripts/compile_locales.sh`
5. Format code: `make lint`
6. Run the bot: `make run`