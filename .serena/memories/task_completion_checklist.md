# Task Completion Checklist

## Before Completing Any Task

### 1. Code Quality Checks
- **MANDATORY**: Run `make lint` (runs both black and isort)
  - This ensures code formatting consistency
  - Both black and isort must pass without errors

### 2. Database Changes
- If models were modified:
  - Generate migrations: `aerich migrate`
  - Apply migrations: `aerich upgrade`
  - Test migration rollback if possible

### 3. Internationalization
- If user-facing text was added/changed:
  - Extract text: `sh scripts/extract_update_locales.sh`
  - Update translation files in `locales/en/` and `locales/ru/`
  - Compile locales: `sh scripts/compile_locales.sh`

### 4. Testing (Manual)
- Start services: `docker-compose up -d`
- Run the bot: `make run`
- Test new functionality manually via Telegram
- Verify no runtime errors in logs

### 5. Dependencies
- If new packages were used, ensure they're added via `poetry add`
- Check that `poetry.lock` is updated

## Critical Notes
- No automated tests are present in the codebase
- Manual testing via Telegram is required
- Always run locale compilation before testing
- Database migrations must be applied before running
- Code must pass both black and isort formatting