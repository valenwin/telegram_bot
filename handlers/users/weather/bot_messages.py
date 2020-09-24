MESSAGES = {
    'weather_for_location_retrieval_failed': 'Не получилось узнать погоду в этой локации 😞,' +
                                             'предлагаем посмотреть, какая погода за окном. \n\n '
                                             '/help - инструкция по использованию бота.',

    'general_failure': 'Я такое не умею 😞.\n\n /help - инструкция по использованию бота.',

    'weather_in_city_message': 'Погода в городе {}:\n{}\nтемпература: {:.1f}°C.',

    'weather_in_location_message': 'Погода в указанной локации:\n{}\nтемпература: {:.1f}°C.',

    'help': 'Я умею показывать погоду в вашем городе, введите название города или отправьте местоположение.'
}


def get_message(message_key: str):
    return MESSAGES[message_key]
