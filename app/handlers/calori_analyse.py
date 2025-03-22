from aiogram import F, Router
from aiogram.types import Message

import app.keyboards as keyboard

calori_analyse_router = Router()
photo_type_keyboard = Router()


@calori_analyse_router.message(F.text == "🍱 Подсчитать калории")
async def calori_analyse(message: Message):
    await message.answer(
        "Выберете тип подсчета калорий:", reply_markup=keyboard.calori_analyse_keyboard
    )
