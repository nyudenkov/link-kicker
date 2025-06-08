# Code Style and Conventions

## Code Formatting
- **Ruff**: Primary linter and formatter (replaced black + isort)
- **Target Python Version**: 3.9+
- All formatting and linting handled by ruff with project-specific configuration

## Code Style Patterns
- Uses async/await extensively for database and API operations
- Type hints are used moderately (not comprehensive)
- Classes use mixins for common functionality (CreatedMixin, UpdatedMixin, ModelMixin)
- Decorators for error handling and intent tracking (`@utils.catch_error`, `@utils.catch_intent`)

## Naming Conventions
- **Variables/Functions**: snake_case
- **Classes**: PascalCase
- **Constants**: UPPER_SNAKE_CASE
- **Database models**: PascalCase with descriptive names (User, Link, StatisticsRecord)

## Import Organization
- Standard library imports first
- Third-party imports second
- Local application imports last
- Relative imports used within app modules
- Import sorting handled automatically by ruff

## Database Patterns
- Uses Tortoise ORM with async patterns
- Models inherit from mixins for common fields
- Class methods for common operations (e.g., `User.get_from_message()`)
- Foreign key relationships properly defined

## Handler Patterns
- Handlers are async functions decorated with error catching
- Use aiogram types for message handling
- Internationalization via `_()` function calls
- Inline keyboards for interactive elements

## Development Workflow
- All Python commands prefixed with `uv run`
- Dependencies managed via uv (not pip or poetry)
- Code quality enforced via `make lint` (ruff)

## No Docstrings
- The codebase does not use docstrings consistently
- Code is self-documenting through clear naming