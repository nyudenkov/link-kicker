# Codebase Structure

## Directory Layout

### Core Application (`app/`)
- **`bot/`** - Telegram bot implementation
  - `handlers/` - Message and callback handlers (start, link, mailing, etc.)
  - `dialogs/` - Complex user interaction flows (feedback, timezone, language)
  - `middlewares/` - Request processing middleware (i18n)
  - `utils/` - Bot utilities (errors, pagination, statistics)
  - `bot.py` - Bot instance configuration
  - `messages.py` - Message generation functions

- **`database/`** - Data layer
  - `models.py` - Database models (User, Link, StatisticsRecord, FeedbackReport)
  - `mixins.py` - Common model functionality
  - `__init__.py` - Tortoise ORM configuration

- **`tasks/`** - Background processing
  - `jobs.py` - Scheduled tasks (mailing, cleanup)
  - `__init__.py` - Scheduler configuration

- **`misc/`** - Utilities and helpers
  - `helper.py` - General utility functions
  - `sentry.py` - Error tracking integration

- **Configuration files**
  - `config.py` - Environment-based configuration
  - `constants.py` - Application constants and messages
  - `enums.py` - Enumerations (Intent, ReportType)

### Scripts (`scripts/`)
- `compile_locales.sh` - Compile translation files
- `extract_update_locales.sh` - Extract and update translations

### Infrastructure
- `main.py` - Application entry point and startup
- `Makefile` - Development commands
- `docker-compose.yml` - Database and Redis services
- `pyproject.toml` - Poetry dependency configuration
- `aerich.ini` - Database migration configuration

### Internationalization (`locales/`)
- `en/LC_MESSAGES/` - English translations
- `ru/LC_MESSAGES/` - Russian translations

### Database (`migrations/`)
- `models/` - SQL migration files

## Key Design Patterns
- **MVC-like structure**: Handlers (controllers), Models (data), Messages (views)
- **Middleware pattern**: For cross-cutting concerns like i18n
- **Dialog pattern**: For complex user interactions
- **Decorator pattern**: For error handling and intent tracking
- **Mixin pattern**: For shared model functionality