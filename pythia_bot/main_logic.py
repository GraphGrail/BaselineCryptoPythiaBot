# coding: utf-8
from __future__ import unicode_literals

USER_NAME = ''

# Функция для непосредственной обработки диалога.
def handle_dialog(request, response, user_storage):
    if request.is_new_session:
        # Это новый пользователь.
        # Инициализируем сессию и приветствуем его.
        user_storage = {
            'suggests': [
                "Какую криптовалюту сейчас стоит держать?",
                "Привет, какая валюта сейчас в негативе?",
                "Покажи негативные твиты про bitcoin",
            ]
        }

        buttons, user_storage = get_suggests(user_storage)
        response.set_text('Привет! Я CryptoPythia, бот компании "GraphGrail", я знаю всё о криптовалютах и могу дать совет :) Просто спроси меня!')
        response.set_buttons(buttons)

        return response, user_storage

    # Обрабатываем ответ пользователя.
    if any(word in request.command.lower() for word in ['покупать', 'купить', 'в позитиве', 'держать', 'ходлить', 'холдить', 'позитивный тренд', 'hodl', 'hold', 'buy', 'in positive']):
        response.set_text('Сейчас проверю, какие криптовалюты сейчас в позитиве!')
        buttons, user_storage = get_suggests(user_storage)
        response.set_buttons(buttons)
        return response, user_storage
    elif any(word in request.command.lower() for word in ['продавать', 'продать', 'в негативе', 'избавиться', 'негативный тренд', 'negative trend']):
        response.set_text('Сейчас проверю, какие валюты сейчас в негативе!')
        buttons, user_storage = get_suggests(user_storage)
        response.set_buttons(buttons)
        return response, user_storage
    elif any(word in request.command.lower() for word in ['твиты', 'твит', 'tweet', 'tweets']):
        given = request.command.lower()
        token = given[given.find(' про ') + len(' про '):].split()[0].strip()
        if token == '':
            token = given[given.find(' о ') + len(' о '):].split()[0].strip()
        if any(sentiment in request.command.lower() for sentiment in ['позитив', 'позитивный', 'позитивные']):
            #API request here
            response.set_text('Вот какие позитивные твиты о ' + token + ' я нашла: ')
        elif any(sentiment in request.command.lower() for sentiment in ['негатив', 'негативный', 'негативные']):
            #API request here
            response.set_text('Вот какие негативные твиты о ' + token + ' я нашла: ')
        buttons, user_storage = get_suggests(user_storage)
        response.set_buttons(buttons)
        return response, user_storage

    buttons, user_storage = get_suggests(user_storage)
    response.set_text('Пожалуйста, повторите Ваш запрос!')
    response.set_buttons(buttons)

    return response, user_storage


def get_suggests(user_storage):
    suggests = [
        {'title': suggest, 'hide': True}
        for suggest in user_storage['suggests']
    ]

    suggests.append({
        "title": 'Перейти на сайт CryptoPythia',
        "url": 'https://cryptopythia.graphgrail.com',
        "hide": True
    })

    return suggests, user_storage
