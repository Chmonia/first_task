import asyncio
from aiogram import Bot, Dispatcher, F
import logging

from aiogram.enums import ContentType
from aiogram.filters import Command
from dotenv import load_dotenv
from core.handlers.basic import get_answer, get_start, get_sticker
from core.settings import settings
from core.utils.commands import set_commands


dp = Dispatcher()


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, F"Бот запущен")


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, F"Бот остановлен")


async def start():
    logging.basicConfig(level=logging.INFO)
    load_dotenv()
    bot = Bot(token=settings.bots.bot_token)
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_sticker, F.content_type == ContentType.STICKER)
    dp.message.register(get_start, Command(commands=["start", "run", "старт"]))
    dp.message.register(get_answer)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
