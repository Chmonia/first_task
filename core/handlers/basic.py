from aiogram import Bot
from aiogram.types import Message


async def get_sticker(message: Message, bot: Bot):
    await message.answer_sticker(message.sticker.file_id)


async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, F"Здравствуйте, {message.from_user.first_name}, рад вас видеть.")


async def get_answer(message: Message, bot: Bot):
    await message.answer(message.text)
