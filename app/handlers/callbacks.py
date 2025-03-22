from aiogram import F, Router
from aiogram.types import CallbackQuery, Message, InaccessibleMessage
import app.keyboards as keyboard

collback_router = Router()


@collback_router.callback_query(F.data == "photo")
async def photo(callback: CallbackQuery):
    await callback.answer()
    if isinstance(callback.message, Message):
        await callback.message.edit_text(
            "Фото блюда или продукта?", reply_markup=keyboard.photo_type_keyboard
        )
    elif isinstance(callback.message, InaccessibleMessage):
        pass


@collback_router.callback_query(F.data == "description")
async def description(callback: CallbackQuery):
    await callback.answer()
    if isinstance(callback.message, Message):
        await callback.message.edit_text(
            "Опишите блюдо или продукт:", reply_markup=None
        )
    elif isinstance(callback.message, InaccessibleMessage):
        pass


@collback_router.callback_query(F.data == "back_to_main_options")
async def back_to_main_options(callback: CallbackQuery):
    await callback.answer()
    if isinstance(callback.message, Message):
        await callback.message.edit_text(
            "Выберете тип подсчета калорий:",
            reply_markup=keyboard.calori_analyse_keyboard,
        )
    elif isinstance(callback.message, InaccessibleMessage):
        pass
