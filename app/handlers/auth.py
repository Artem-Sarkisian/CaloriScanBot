from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from app.handlers.states import Login
import app.keyboards as keyboard


auth_router = Router()


@auth_router.message(F.text == "📝 Дневник питания")
@auth_router.message(F.text == "📊 Статистика")
async def auth_message(message: Message, state: FSMContext):
    await message.answer(
        "Для доступа к этой функции вам необходимо авторизоваться",
        reply_markup=keyboard.auth_keyboard,
    )


@auth_router.callback_query(F.data == "login")
async def login(callback: CallbackQuery, state: FSMContext):    
    await callback.answer()
    if callback.message:
        await state.set_state(Login.email)
        await callback.message.answer("Введите ваш email:", reply_markup=None)



@auth_router.message(Login.email)
async def login_process_email(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    await state.set_state("Login.password")
    await message.answer("Введите ваш пароль:", reply_markup=None)


@auth_router.message(Login.password)
async def login_process_password(message: Message, state: FSMContext):
    await state.update_data(password=message.text)
    user_data = await state.get_data()
    
    if verify_user(user_data["email"], user_data["password"]): # type: ignore
        await state.clear()
        await message.answer(
            "Вы успешно авторизованы!", reply_markup=keyboard.main_keyboard
        )
    else:
        await message.answer(
            "Неверный email или пароль. Попробуйте снова.",
            reply_markup=keyboard.auth_keyboard,
        )
