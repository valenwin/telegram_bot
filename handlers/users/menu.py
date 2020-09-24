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


@dp.message_handler(Text(equals=['😂', '😎', '🤯']))
async def get_book(message: types.Message):
    if message.text == '😂':
        await message.answer('Так счастлив, что аж проливает слезы радости. '
                             'Имеет приступ смеха и не может сдержать себя.',
                             reply_markup=ReplyKeyboardRemove())
    elif message.text == '😎':
        await message.answer('Я король мира! Мистер крутой смайлик в солнцезащитных очках. '
                             'Полностью уверен в себе и расслаблен. Все абсолютно легко и круто.',
                             reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer('«Грибное» облако. Иногда у вас бывают дни, когда вы понимаете, '
                             'что никогда ранее не осознавали. Вы осознаете те моменты, '
                             'которые заставляют задуматься и помогают дать ответ на вопрос'
                             ' "почему я никогда этого не замечал?"',
                             reply_markup=ReplyKeyboardRemove())
