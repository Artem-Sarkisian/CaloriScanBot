from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

import app.database.requests as db_requests
import app.keyboards as keyboard

base_router = Router()


@base_router.message(CommandStart())
async def start(message: Message):
    if message.from_user:
        await db_requests.start_user(
            tg_id=message.from_user.id,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name or "",
            username=message.from_user.username or "",
        )
    await message.answer("Hello! I'm a bot!", reply_markup=keyboard.main_keyboard)


@base_router.message(Command("help"))
async def help(message: Message):
    await message.answer("Help message")
