import os
import django
from apps.bot.config import bot, dp
from aiogram import types
import logging

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

django.setup()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Hello World!')
