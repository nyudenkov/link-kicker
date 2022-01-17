from aiogram import Bot

from app import config

bot = Bot(config.BOT_TOKEN, parse_mode="html")
