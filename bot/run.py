# -*- coding: utf-8 -*-


import time
import logging

from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup

from src import config
from src.ui_dispatch import dispatch
import src.generators.ui as main

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# id:state
chats = {}


def send_error(chat_id):
    key_board = ReplyKeyboardMarkup()
    key_board.add(*main.buttons.get('start'))
    bot.send_message(chat_id=chat_id, text=main.greetings.get('error'), reply_markup=key_board)


def listener(messages):
    for m in messages:
        if m.content_type == 'text':
            try:
                logging.debug(u'Chat with id {0} send message {1}'.format(m.chat.id, m.text))
                m.text = m.text[12:] if m.text.startswith('@gen_ru_bot') else m.text
                message_dispatched = dispatch(bot, chats, m.chat.id, m.text)

                if not message_dispatched:
                    logging.warning(
                        u'Message is not dispatched (chat id - {0}) | message: {1}'.format(m.chat.id, m.text))
                    send_error(m.chat.id)

            except Exception as e:
                if chats.get(m.chat.id) is not None:
                    del chats[m.chat.id]
                logging.error(u'Error by chat with id {0} | error: {1}'.format(m.chat.id, e))
                send_error(m.chat.id)


def callback_listener(call):
    logger.info(call)
    try:
        message_dispatched = dispatch(bot, chats, call.from_user.id, call.data, call.message.message_id)

        if not message_dispatched:
            logging.warning(
                u'Message2 is not dispatched (chat id - {0}) | message: {1}'.format(call.from_user.id, call.data))
            send_error(call.from_user.id)

    except Exception as e:
        if chats.get(call.from_user.id) is not None:
            del chats[call.from_user.id]
        logging.error(u'Error2 by chat with id {0} | error: {1}'.format(call.from_user.id, e))
        send_error(call.from_user.id)


if __name__ == '__main__':
    bot = TeleBot(config.token)
    bot.set_update_listener(listener)

    @bot.callback_query_handler(func=lambda call: True)
    def test_callback(call):
        callback_listener(call)

    bot.polling(none_stop=True)
    while True:
        time.sleep(200)
