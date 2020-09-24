from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Book1')
        ],
        [
            KeyboardButton(text='Book2'),
            KeyboardButton(text='Book3'),
        ],
    ],
    resize_keyboard=True
)
