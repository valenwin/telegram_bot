from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_dates import currency_callback

choice = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text='USD',
                                          callback_data=currency_callback.new(item_name='dollar')
                                      ),
                                      InlineKeyboardButton(
                                          text='EUR',
                                          callback_data='buy:euro'
                                      ),
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text='Cancel',
                                          callback_data='cancel'
                                      )
                                  ]
                              ])

usd_keyboard = InlineKeyboardMarkup()
USD_LINK = 'https://minfin.com.ua/currency/kiev/usd/'
usd_link = InlineKeyboardButton(text='USD Exchange Rate',
                                url=USD_LINK)
usd_keyboard.insert(usd_link)

eur_keyboard = InlineKeyboardMarkup()
EUR_LINK = 'https://minfin.com.ua/currency/kiev/eur/'
eur_link = InlineKeyboardButton(text='EUR Exchange Rate',
                                url=EUR_LINK)
eur_keyboard.insert(eur_link)
