# Aiogram v3 Migration Plan

This document outlines the plan for migrating from aiogram v2.22.1 to v3.21.0.

## Migration Status: Core Structure Complete ✅

### Dependencies ✅
- aiogram: 2.22.1 → 3.21.0
- aiogram-dialog: 1.9.0 → 2.4.0

### Key Components Migrated ✅

#### 1. **main.py** ✅
- ✅ Replaced `executor.start_polling()` with `asyncio.run()` and `dp.start_polling()`
- ✅ Updated imports for aiogram v3
- ✅ Updated startup/shutdown logic

#### 2. **Bot initialization** ✅
- ✅ Updated to use `ParseMode.HTML` enum instead of string
- ✅ Updated helper functions to accept Bot instance

#### 3. **Handlers** ✅
- ✅ Migrated from `dp.register_*_handler()` to Router pattern
- ✅ Created `main_router` and registered with dispatcher
- ✅ Updated filters to use function-based filters instead of lambda expressions
- ✅ Updated imports

#### 4. **Middlewares** ✅
- ✅ Rewrote I18nMiddleware to extend BaseMiddleware
- ✅ Updated middleware registration to use `dispatcher.message.middleware()`
- ✅ Removed deprecated LoggingMiddleware
- ✅ Updated type annotations to modern Python syntax

#### 5. **Dialog System** ✅
- ✅ Updated imports (`aiogram.fsm.state` instead of `aiogram.dispatcher.filters.state`)
- ✅ Updated exception handling (`TelegramBadRequest` instead of `MessageNotModified`)  
- ✅ Updated dialog registration to include routers in dispatcher
- ✅ Updated ContentType import to use `aiogram.enums.ContentType`

#### 6. **Code Quality** ✅
- ✅ Fixed all linting issues (import organization, type annotations, line lengths)
- ✅ Updated type annotations to use modern Python syntax (`dict` instead of `Dict`)
- ✅ Removed unused imports
- ✅ All ruff checks passing

## Testing Required

### Installation Test
```bash
# Install the new dependencies
pip install aiogram==3.21.0 aiogram-dialog==2.4.0

# Test basic imports
python -c "import aiogram; print(f'aiogram {aiogram.__version__}')"
python -c "import aiogram_dialog; print('aiogram-dialog imported successfully')"
```

### Functionality Tests
1. **Basic bot startup** - Test if the bot can start without errors
2. **Command handlers** - Test /start, /language, etc.
3. **Dialog system** - Test language selection and other dialogs
4. **i18n functionality** - Test translation system
5. **Callback handlers** - Test link management callbacks

## Key Migration Notes

### Breaking Changes Addressed
- ✅ `executor` → `asyncio.run()` with `dp.start_polling()`
- ✅ Handler registration → Router pattern
- ✅ Middleware API → BaseMiddleware
- ✅ State imports → `aiogram.fsm.state`
- ✅ Exception imports → `aiogram.exceptions`
- ✅ ContentType → `aiogram.enums.ContentType`
- ✅ ParseMode → `aiogram.enums.ParseMode`

### I18n System Special Attention
As requested, special care was taken with i18n changes:
- ✅ Completely rewrote I18nMiddleware for v3 compatibility
- ✅ Maintained existing language selection functionality
- ✅ Preserved custom language data structure
- ✅ Updated gettext integration
- ✅ Ensured backward compatibility with existing translations

## Files Modified
- `pyproject.toml` - Updated dependencies
- `main.py` - Core application structure
- `app/bot/bot.py` - Bot initialization
- `app/misc/helper.py` - Helper functions
- `app/bot/handlers/__init__.py` - Handler registration
- `app/bot/handlers/start.py` - Start handler updates
- `app/bot/middlewares/__init__.py` - Middleware setup
- `app/bot/middlewares/i18n.py` - I18n middleware rewrite
- `app/bot/dialogs/__init__.py` - Dialog registration
- `app/bot/dialogs/language.py` - Language dialog updates
- `app/bot/dialogs/feedback.py` - State import updates
- `app/bot/dialogs/hour.py` - State import updates
- `app/bot/dialogs/timezone.py` - State and ContentType import updates

The migration is structurally complete and ready for testing once the new dependencies are installed.