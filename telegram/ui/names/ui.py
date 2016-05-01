# -*- coding: utf-8 -*-


from telebot.types import ReplyKeyboardMarkup
from telebot.types import KeyboardButton


from telegram.generators.generator import generate
from telegram.ui.main import ui as main


greetings = {
    'names_sex': 'Выберите пол',
    'names_field': 'Выберите необходимые поля',
    'names_count': 'Выберите количество имен'
}


menus = {
    'names_sex': ['М', 'Ж', 'Все ровно', 'Nicknames', 'Просто сделай это', 'Меню'],
    'names_field': ['ФИО', 'Ф', 'И', 'О', 'ФИ', 'ИО', 'Просто сделай это', 'Меню'],
    'names_count': ['1', '10', '100', 'Просто сделай это', 'Меню']
}


def dispatch(bot, chats, chat_id, command):
    key_board = ReplyKeyboardMarkup()
    command = command.strip()
    chat = chats.get(chat_id) if chats.get(chat_id) is not None else {}
    if command == 'Имена' or command == 'names':
        chat['processor'] = 'names'
        key_board.add(*map(lambda text: KeyboardButton(text), menus.get('names_sex')))
        bot.send_message(chat_id=chat_id, text=greetings.get('names_sex'), reply_markup=key_board)
        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'names' and chat.get('sex') is None:
        if command == 'М':
            command = 'man'
        elif command == 'Ж':
            command = 'woman'
        elif command == 'Все ровно':
            command = 'all'
        elif command == 'Nicknames':
            command = 'nick'
        chat['sex'] = command
        if command == 'nick':
            key_board.add(*map(lambda text: KeyboardButton(text), menus.get('names_count')))
            bot.send_message(chat_id=chat_id, text=greetings.get('names_count'), reply_markup=key_board)
        else:
            key_board.add(*map(lambda text: KeyboardButton(text), menus.get('names_field')))
            bot.send_message(chat_id=chat_id, text=greetings.get('names_field'), reply_markup=key_board)
        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'names' and chat.get('sex') is not None and chat.get('sex') != 'nick' and \
            chat.get('surname') is None and chat.get('name') is None and chat.get('patronymic') is None:
        chat['surname'] = '0'
        chat['name'] = '0'
        chat['patronymic'] = '0'
        if command == 'ФИО':
            chat['surname'] = '1'
            chat['name'] = '1'
            chat['patronymic'] = '1'
        elif command == 'Ф':
            chat['surname'] = '1'
        elif command == 'И':
            chat['name'] = '1'
        elif command == 'О':
            chat['patronymic'] = '1'
        elif command == 'ФИ':
            chat['surname'] = '1'
            chat['name'] = '1'
        elif command == 'ИО':
            chat['name'] = '1'
            chat['patronymic'] = '1'
        key_board.add(*map(lambda text: KeyboardButton(text), menus.get('names_count')))
        bot.send_message(chat_id=chat_id, text=greetings.get('names_count'), reply_markup=key_board)
        return True
    elif chat.get('processor') == 'names' and chat.get('count') is None:
        chat['count'] = command
        chats[chat_id] = chat
        key_board.add(*map(lambda text: KeyboardButton(text), main.menus.get('main')))
        bot.send_message(chat_id=chat_id, text=generate(chat), reply_markup=key_board)
        del chats[chat_id]
        return True
    return False
