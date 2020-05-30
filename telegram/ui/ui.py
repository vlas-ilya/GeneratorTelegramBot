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
    lambda bot, chats, chat_id, command, message_id: main.dispatch(bot, chats, chat_id, command, message_id),
    lambda bot, chats, chat_id, command, message_id: compliments.dispatch(bot, chats, chat_id, command, message_id),
    lambda bot, chats, chat_id, command, message_id: facts.dispatch(bot, chats, chat_id, command, message_id),
    lambda bot, chats, chat_id, command, message_id: inn.dispatch(bot, chats, chat_id, command, message_id),
    lambda bot, chats, chat_id, command, message_id: jokes.dispatch(bot, chats, chat_id, command, message_id),
    lambda bot, chats, chat_id, command, message_id: names.dispatch(bot, chats, chat_id, command, message_id),
    lambda bot, chats, chat_id, command, message_id: numbers.dispatch(bot, chats, chat_id, command, message_id),
    lambda bot, chats, chat_id, command, message_id: passwords.dispatch(bot, chats, chat_id, command, message_id),
    lambda bot, chats, chat_id, command, message_id: quotes.dispatch(bot, chats, chat_id, command, message_id),
    lambda bot, chats, chat_id, command, message_id: text.dispatch(bot, chats, chat_id, command, message_id)
]


def dispatch(bot, chats, chat_id, command, message_id=None):
    return any(dispatcher(bot, chats, chat_id, command, message_id) for dispatcher in dispatchers)
