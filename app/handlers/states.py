from aiogram.filters.state import State, StatesGroup


class CaloriAnalyze(StatesGroup):
    photo_dish = State()
    photo_product = State()
    description = State()


class Register(StatesGroup):
    name = State()
    email = State()
    phone = State()
    password = State()
    confirm_password = State()


class Login(StatesGroup):
    email = State()
    password = State()


class ForgotPassword(StatesGroup):
    email = State()
    new_password = State()


class ChangePassword(StatesGroup):
    old_password = State()
    new_password = State()
    confirm_password = State()
