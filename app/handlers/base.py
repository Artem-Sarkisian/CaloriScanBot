from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram import Router
import app.keyboards as keyboard

base_router = Router()


@base_router.message(CommandStart())
async def start(message: Message):
    await message.answer("Hello! I'm a bot!", reply_markup=keyboard.main_keyboard)


@base_router.message(Command("help"))
async def help(message: Message):
    await message.answer("Help message")
