# Testing the Aiogram v3 Migration

This document provides instructions for testing the completed migration.

## Prerequisites

The migration is structurally complete but requires installation of the new dependencies to test.

## Installation

```bash
# Install the new dependencies
pip install aiogram==3.21.0 aiogram-dialog==2.4.0

# Or if using uv (recommended)
uv sync
```

## Basic Import Tests

Test that the core modules can be imported:

```bash
# Test aiogram v3 import
python -c "import aiogram; print(f'aiogram {aiogram.__version__}')"

# Test aiogram-dialog v2 import  
python -c "import aiogram_dialog; print('aiogram-dialog imported successfully')"

# Test main module import
python -c "from main import main; print('Main module imported successfully')"

# Test bot import
python -c "from app.bot.bot import bot; print('Bot imported successfully')"

# Test middleware import
python -c "from app.bot.middlewares import i18n; print('i18n middleware imported successfully')"
```

## Functionality Tests

### 1. Bot Startup Test
```bash
# Test if bot can start (will fail without valid token, but should not have import errors)
python main.py
```

### 2. Handler Registration Test
Check that all handlers are properly registered:
```bash
python -c "
from main import dp
print('Registered message handlers:', len(dp.message.handlers))
print('Registered callback handlers:', len(dp.callback_query.handlers))
"
```

### 3. Dialog System Test
Test dialog imports and registration:
```bash
python -c "
from app.bot.dialogs import language_dialog, feedback_dialog
print('Dialogs imported successfully')
"
```

### 4. I18n Middleware Test
Test the rewritten i18n middleware:
```bash
python -c "
from app.bot.middlewares.i18n import I18nMiddleware
middleware = I18nMiddleware('link_kicker', default='en')
print('Available languages:', list(middleware.AVAILABLE_LANGUAGES.keys()))
print('Default locale:', middleware.default)
"
```

## Expected Results

### ✅ Success Indicators
- All imports work without ModuleNotFoundError
- No ImportError exceptions
- Bot can initialize (even without token)
- Handlers are registered correctly
- Dialogs can be imported
- i18n middleware initializes properly

### ❌ Failure Indicators  
- ImportError or ModuleNotFoundError
- Syntax errors in any module
- Missing handler registrations
- Dialog import failures
- i18n middleware initialization errors

## Troubleshooting

### Common Issues

1. **ModuleNotFoundError: No module named 'aiogram'**
   - Solution: Install aiogram v3 with `pip install aiogram==3.21.0`

2. **Import errors in dialogs**
   - Check that all `aiogram.fsm.state` imports are correct
   - Verify `aiogram.enums.ContentType` imports

3. **Middleware registration errors**
   - Ensure BaseMiddleware is properly extended
   - Check middleware registration syntax

4. **Handler registration issues**
   - Verify Router pattern is used correctly
   - Check filter function definitions

## Next Steps After Testing

Once basic imports and functionality work:

1. Test with actual bot token
2. Test all command handlers (/start, /language, etc.)
3. Test dialog flows
4. Test callback query handlers
5. Verify i18n translations work correctly
6. Test all user-facing features

## Migration Completion Criteria

- [ ] All modules import successfully
- [ ] Bot starts without errors
- [ ] All handlers are registered
- [ ] Dialog system works
- [ ] I18n system functions correctly
- [ ] No regression in user-facing features