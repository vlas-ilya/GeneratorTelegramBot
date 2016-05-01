# -*- coding: utf-8 -*-


import telegram.ui.main.ui as main
import telegram.ui.compliments.ui as compliments
import telegram.ui.facts.ui as facts
import telegram.ui.inn.ui as inn
import telegram.ui.jokes.ui as jokes
import telegram.ui.names.ui as names
import telegram.ui.numbers.ui as numbers
import telegram.ui.passwords.ui as passwords
import telegram.ui.quotes.ui as quotes
import telegram.ui.text.ui as text


dispatchers = [
    lambda bot, chats, chat_id, command: main.dispatch(bot, chats, chat_id, command),
    lambda bot, chats, chat_id, command: compliments.dispatch(bot, chats, chat_id, command),
    lambda bot, chats, chat_id, command: facts.dispatch(bot, chats, chat_id, command),
    lambda bot, chats, chat_id, command: inn.dispatch(bot, chats, chat_id, command),
    lambda bot, chats, chat_id, command: jokes.dispatch(bot, chats, chat_id, command),
    lambda bot, chats, chat_id, command: names.dispatch(bot, chats, chat_id, command),
    lambda bot, chats, chat_id, command: numbers.dispatch(bot, chats, chat_id, command),
    lambda bot, chats, chat_id, command: passwords.dispatch(bot, chats, chat_id, command),
    lambda bot, chats, chat_id, command: quotes.dispatch(bot, chats, chat_id, command),
    lambda bot, chats, chat_id, command: text.dispatch(bot, chats, chat_id, command)
]


def dispatch(bot, chats, chat_id, command):
    return any(dispatcher(bot, chats, chat_id, command) for dispatcher in dispatchers)
