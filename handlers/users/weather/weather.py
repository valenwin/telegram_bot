import logging

from aiogram import types

from handlers.users.weather.advice_service import get_advice
from handlers.users.weather.bot_messages import get_message
from handlers.users.weather.weather_service import WeatherServiceException, WeatherInfo, get_weather_for_city, \
    get_weather_for_location
from loader import dp

WEATHER_RETRIEVAL_FAILED_MESSAGE = get_message('weather_for_location_retrieval_failed')

logging.basicConfig(level=logging.INFO)


@dp.message_handler(content_types=['text'])
async def get_weather_in_city(message: types.Message):
    try:
        weather: WeatherInfo = await get_weather_for_city(message.text)
    except WeatherServiceException:
        await message.reply(WEATHER_RETRIEVAL_FAILED_MESSAGE)
        return

    response = get_message('weather_in_city_message') \
                   .format(message.text, weather.status, weather.temperature) + '\n\n' + \
               get_advice(weather)

    await message.reply(response)


@dp.message_handler()
async def default_response(message: types.Message):
    await message.reply(get_message('general_failure'))


@dp.message_handler(content_types=['location'])
async def get_weather_in_location(message: types.Message):
    if message.location:
        try:
            weather = await get_weather_for_location(message.location)
        except WeatherServiceException:
            await message.reply(WEATHER_RETRIEVAL_FAILED_MESSAGE)
            return

        response = get_message('weather_in_location_message') \
                       .format(weather.status, weather.temperature) + '\n\n' + \
                   get_advice(weather)

        await message.reply(response)
        return

    await message.reply(WEATHER_RETRIEVAL_FAILED_MESSAGE)
