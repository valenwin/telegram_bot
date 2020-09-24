from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_dates import buy_callback

choice = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text='Buy items',
                                          callback_data=buy_callback.new(item_name='item',
                                                                         quantity=1)
                                      ),
                                      InlineKeyboardButton(
                                          text='Buy items2',
                                          callback_data='buy:item2:10'
                                      ),
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text='Cancel',
                                          callback_data='cancel'
                                      )
                                  ]
                              ])

item_keyboard = InlineKeyboardMarkup()
ITEM_LINK = 'https://rozetka.com.ua/lg_32lm6300pla/p108548406/'
item_link = InlineKeyboardButton(text='Link for buying',
                                 url=ITEM_LINK)
item_keyboard.insert(item_link)


item2_keyboard = InlineKeyboardMarkup()
ITEM2_LINK = 'https://rozetka.com.ua/samsung_ue32n4000auxua/p46830216/'
item2_link = InlineKeyboardButton(text='Link for buying',
                                  url=ITEM2_LINK)
item2_keyboard.insert(item2_link)
