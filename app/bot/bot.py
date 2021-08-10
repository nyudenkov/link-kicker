from aiogram import Bot

from app import config

bot = Bot(**config.get("bot"))
