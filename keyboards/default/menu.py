from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='😂'),
            KeyboardButton(text='🤯'),
            KeyboardButton(text='😎'),
        ],
    ],
    resize_keyboard=True
)
