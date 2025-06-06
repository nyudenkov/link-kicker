# Suggested Development Commands

## Essential Commands for Development

### Package Management
- `poetry install` - Install dependencies
- `poetry add <package>` - Add a new dependency
- `poetry add --dev <package>` - Add a development dependency

### Code Quality
- `make lint` - Run both black and isort formatting (recommended before commits)
- `make black` - Format code with black
- `make isort` - Sort imports with isort
- `python -m black .` - Alternative way to run black
- `python -m isort .` - Alternative way to run isort

### Database Operations
- `aerich upgrade` - Apply database migrations
- `aerich migrate` - Generate new migrations from model changes
- `aerich init-db` - Initialize database schema

### Internationalization
- `sh scripts/extract_update_locales.sh` - Extract and update translation files
- `sh scripts/compile_locales.sh` - Compile locale files (required before running)

### Running the Application
- `make run` - Start the bot (equivalent to `python -m main`)
- `python -m main` - Alternative way to start the bot

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
2. Install dependencies: `poetry install`
3. Apply migrations: `aerich upgrade`
4. Compile locales: `sh scripts/compile_locales.sh`
5. Format code: `make lint`
6. Run the bot: `make run`