import logging

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.inline.callback_dates import buy_callback
from keyboards.inline.choice_buttons import choice, item_keyboard, item2_keyboard
from loader import dp


@dp.message_handler(Command('items'))
async def show_items(message: types.Message):
    await message.answer(text='There are 2 items. '
                              'Press Cancel if you don\'t need anything',
                         reply_markup=choice)


@dp.callback_query_handler(buy_callback.filter(item_name='item'))
async def buying_item(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f'callback_data={call.data}')
    logging.info(f'callback_data dict={callback_data}')
    quantity = callback_data.get('quantity')
    await call.message.answer(f'You have chosen item. There are {quantity} items',
                              reply_markup=item_keyboard)


@dp.callback_query_handler(buy_callback.filter(item_name='item2'))
async def buying_item2(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f'callback_data={call.data}')
    logging.info(f'callback_data dict={callback_data}')
    quantity = callback_data.get('quantity')
    await call.message.answer(f'You have chosen item2. There are {quantity} items',
                              reply_markup=item2_keyboard)


@dp.callback_query_handler(text='cancel')
async def cancel(call: CallbackQuery):
    await call.answer('You have canceled your purchase.',
                      show_alert=True)
    await call.message.edit_reply_markup()
