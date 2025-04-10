from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton,
                           ReplyKeyboardRemove)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


seller_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Профиль"),
            KeyboardButton(text="Мои проекты"),
            KeyboardButton(text="Добавить проект"),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Выберите пункт меню...'
)

buyer_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Профиль"),
            KeyboardButton(text="Список проектов")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Выберите пункт меню...'
)

main_menu = {
    "seller": seller_main_menu,
    "buyer": buyer_main_menu,
}
