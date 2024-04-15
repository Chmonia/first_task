from aiogram import Bot
from aiogram.types import Message
import datetime as dt


async def get_sticker(message: Message, bot: Bot):
    await message.answer_sticker(message.sticker.file_id)


async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, F"Здравствуйте, {message.from_user.first_name}, рад вас видеть.")


async def get_answer(message: Message, bot: Bot):
    await message.answer(message.text)


async def command_help(message: Message, bot: Bot):
    await message.answer(f"Я пока не умею помогать...")


async def command_data(message: Message):
    await message.answer(f"{dt.date.today().isoformat()} - сегодняшняя дата")


async def command_time(message: Message):
    time = dt.datetime.now()
    await message.answer(f"{time.strftime('%H:%M:%S')} - время сейчас")
