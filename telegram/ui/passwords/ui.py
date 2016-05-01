# -*- coding: utf-8 -*-


from telebot.types import ReplyKeyboardMarkup
from telebot.types import KeyboardButton


from telegram.generators.generator import generate
from telegram.ui.main import ui as main


greetings = {
    'passwords_count': 'Выберите колличество символов в пароле',
    'passwords_type': 'Выберите состав символов в пароле'
}


menus = {
    'passwords_count': ['6', '10', '14', 'Просто сделай это', 'Меню'],
    'passwords_type': ['Буквы и Цифры', 'Буквы', 'Буквы, Цифры и Символы', 'Просто сделай это', 'Меню']
}


def dispatch(bot, chats, chat_id, command):
    key_board = ReplyKeyboardMarkup()
    command = command.strip()
    chat = chats.get(chat_id) if chats.get(chat_id) is not None else {}
    if command == 'Пароли' or command == 'passwords':
        chat['processor'] = 'passwords'
        key_board.add(*map(lambda text: KeyboardButton(text), menus.get('passwords_count')))
        bot.send_message(chat_id=chat_id, text=greetings.get('passwords_count'), reply_markup=key_board)
        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'passwords' and chat.get('count') is None:
        chat['count'] = command
        key_board.add(*map(lambda text: KeyboardButton(text), menus.get('passwords_type')))
        bot.send_message(chat_id=chat_id, text=greetings.get('passwords_type'), reply_markup=key_board)
        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'passwords' and chat.get('count') is not None:
        chat['upper'] = '0'
        chat['lower'] = '0'
        chat['num'] = '0'
        chat['symbol'] = '0'
        if command == 'Буквы и Цифры':
            chat['upper'] = '1'
            chat['lower'] = '1'
            chat['num'] = '1'
        elif command == 'Буквы':
            chat['upper'] = '1'
            chat['lower'] = '1'
        elif command == 'Буквы, Цифры и Символы':
            chat['upper'] = '1'
            chat['lower'] = '1'
            chat['num'] = '1'
            chat['symbol'] = '1'
        chats[chat_id] = chat
        key_board.add(*map(lambda text: KeyboardButton(text), main.menus.get('main')))
        bot.send_message(chat_id=chat_id, text=generate(chat), reply_markup=key_board)
        del chats[chat_id]
        return True
    return False
