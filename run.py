# -*- coding: utf-8 -*-


import time


from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup
from telebot.types import KeyboardButton


from telegram import config
from telegram.ui.ui import dispatch
from telegram.ui.main.ui import menus


# id:state
chats = {}


def send_error(chat_id):
    key_board = ReplyKeyboardMarkup()
    key_board.add(*map(lambda text: KeyboardButton(text), menus.get('main')))
    bot.send_message(chat_id=chat_id, text="Что-то пошло не так", reply_markup=key_board)


def listener(messages):
    for m in messages:
        if m.content_type == 'text':
            try:
                m.text = m.text[12:] if m.text.startswith('@gen_ru_bot') else m.text
                message_dispatched = dispatch(bot, chats, m.chat.id, m.text)
                if not message_dispatched:
                    send_error(m.chat.id)
            except Exception:
                send_error(m.chat.id)


if __name__ == '__main__':
    bot = TeleBot(config.token)
    bot.set_update_listener(listener)
    bot.polling(none_stop=True)
    while True:
        time.sleep(200)
