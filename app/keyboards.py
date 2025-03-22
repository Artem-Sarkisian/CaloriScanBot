from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

auth_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Войти", callback_data="login"),
            InlineKeyboardButton(text="Зарегистрироваться", callback_data="register"),
        ]
    ]
)

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🍱 Подсчитать калории")],
        [
            KeyboardButton(text="📝 Дневник питания"),
            KeyboardButton(text="📊 Статистика"),
        ],
        [KeyboardButton(text="📚 Помощь")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите действие:",
)

calori_analyse_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📷 По фото", callback_data="photo"),
            InlineKeyboardButton(text="📄 По описанию", callback_data="description"),
        ],
        [InlineKeyboardButton(text="📚 Помощь", callback_data="help")],
    ]
)

photo_type_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📷 Фото блюда", callback_data="photo_dish"),
            InlineKeyboardButton(
                text="🥬 Фото продукта", callback_data="photo_product"
            ),
        ],
        [InlineKeyboardButton(text="◀️ Назад", callback_data="back_to_main_options")],
    ]
)
