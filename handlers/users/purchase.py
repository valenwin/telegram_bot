import logging
from datetime import datetime

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.inline.callback_dates import currency_callback
from keyboards.inline.choice_buttons import choice, usd_keyboard, eur_keyboard
from loader import dp


@dp.message_handler(Command('exchange'))
async def show_exchange(message: types.Message):
    await message.answer(text='There are 2 types of currency. '
                              'Press Cancel to exit from inline menu.',
                         reply_markup=choice)


@dp.callback_query_handler(currency_callback.filter(item_name='dollar'))
async def exchange_rate_dollar(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f'callback_data={call.data}')
    logging.info(f'callback_data dict={callback_data}')
    await call.message.answer(f'You have chosen USD. '
                              f'Current datetime {datetime.now().strftime("%d-%m-%Y, %H:%M:%S")}',
                              reply_markup=usd_keyboard)


@dp.callback_query_handler(currency_callback.filter(item_name='euro'))
async def exchange_rate_euro(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f'callback_data={call.data}')
    logging.info(f'callback_data dict={callback_data}')
    await call.message.answer(f'You have chosen EUR. '
                              f'Current datetime {datetime.now().strftime("%d-%m-%Y, %H:%M:%S")}',
                              reply_markup=eur_keyboard)


@dp.callback_query_handler(text='cancel')
async def cancel(call: CallbackQuery):
    await call.answer('You closed inline menu.',
                      show_alert=True)
    await call.message.edit_reply_markup()
