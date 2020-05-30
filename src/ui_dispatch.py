# -*- coding: utf-8 -*-


import src.generators.ui as main
import src.generators.compliments.ui as compliments
import src.generators.facts.ui as facts
import src.generators.inn.ui as inn
import src.generators.jokes.ui as jokes
import src.generators.names.ui as names
import src.generators.numbers.ui as numbers
import src.generators.passwords.ui as passwords
import src.generators.quotes.ui as quotes
import src.generators.text.ui as text


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
