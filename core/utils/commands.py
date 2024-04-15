from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command="start",
            description="Начало работы бота ↩"
        ),
        BotCommand(
            command="help",
            description="Помощь"
        ),
        BotCommand(
            command="time",
            description="текущее время в текстовом формате"
        ),
        BotCommand(
            command="date",
            description="текущяя дата в текстовом формате"
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
