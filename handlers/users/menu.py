from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import menu
from loader import dp


@dp.message_handler(Command('menu'))
async def show_menu(message: types.Message):
    await message.answer(
        'Choose the product from the menu:',
        reply_markup=menu
    )


@dp.message_handler(Text(equals=['Book1', 'Book2', 'Book3']))
async def get_book(message: types.Message):
    await message.answer(f'You have chosen: {message.text}',
                         reply_markup=ReplyKeyboardRemove())