# Link Kicker - Project Overview

## Purpose
Link Kicker is a Telegram bot that helps users remember to read articles they've saved links to. The bot sends scheduled reminders to users about their saved links to prevent them from forgetting about articles they intended to read.

## Tech Stack
- **Language**: Python 3.9+
- **Bot Framework**: aiogram (v2.13) - Telegram Bot API framework
- **Database**: PostgreSQL with Tortoise ORM (async)
- **Task Scheduling**: APScheduler for sending reminders
- **Cache/Session**: Redis for caching and sessions
- **Async Framework**: asyncio-based architecture
- **Internationalization**: babel for locale management (supports English and Russian)
- **Error Tracking**: Sentry integration
- **Dialog Management**: aiogram-dialog for complex user interactions
- **Geographic**: timezonefinder for timezone detection

## Key Features
- Save links from messages
- Scheduled link reminders via mailing system
- User preferences (timezone, hour, language)
- Link management (view, delete, mark as read)
- User statistics and feedback system
- Multilingual support (en/ru)

## Architecture
The project follows a modular structure:
- `app/bot/` - Bot handlers, dialogs, and messaging logic
- `app/database/` - Database models and ORM configuration
- `app/tasks/` - Background jobs and scheduling
- `app/misc/` - Utilities and helper functions
- `locales/` - Internationalization files
- `migrations/` - Database migration scripts