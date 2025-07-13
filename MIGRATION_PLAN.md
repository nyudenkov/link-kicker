# Aiogram v3 Migration Plan

This document outlines the plan for migrating from aiogram v2.22.1 to v3.21.0.

## Current State Analysis

### Dependencies
- aiogram: 2.22.1 (needs upgrade to 3.21.0)
- aiogram-dialog: 1.9.0 (needs upgrade to 2.4.0)

### Key Components Using aiogram v2 API
1. **main.py**: Uses `executor.start_polling()` pattern
2. **Bot initialization**: Basic Bot() initialization
3. **Handlers**: Uses `dp.register_*_handler()` pattern
4. **Middlewares**: Uses old middleware setup pattern
5. **Dialogs**: Uses aiogram-dialog v1 API

## Migration Steps

### Phase 1: Dependencies
- [ ] Update pyproject.toml dependencies
- [ ] Test dependency compatibility

### Phase 2: Core Application Structure
- [ ] Replace executor with Application pattern
- [ ] Update main.py startup/shutdown logic
- [ ] Update bot initialization

### Phase 3: Handlers and Routers
- [ ] Migrate handler registration to router pattern
- [ ] Update handler function signatures if needed
- [ ] Test handler functionality

### Phase 4: Middlewares
- [ ] Update middleware registration
- [ ] Migrate i18n middleware to v3 API
- [ ] Test middleware functionality

### Phase 5: Dialog System
- [ ] Update dialog imports and API usage
- [ ] Test dialog functionality
- [ ] Verify i18n integration with dialogs

### Phase 6: Testing and Validation
- [ ] Run linting and type checking
- [ ] Test all bot commands
- [ ] Verify no regression in functionality

## Notes
- Pay special attention to i18n changes as requested
- Ensure minimal breaking changes to user experience
- Test thoroughly before marking as complete