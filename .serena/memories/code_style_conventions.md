# Code Style and Conventions

## Code Formatting
- **Black**: Code formatter with default settings
- **isort**: Import sorting and organization
- **Target Python Version**: 3.9+

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

## No Docstrings
- The codebase does not use docstrings consistently
- Code is self-documenting through clear naming