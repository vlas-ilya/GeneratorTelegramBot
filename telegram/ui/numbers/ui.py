# -*- coding: utf-8 -*-


from telebot.types import ReplyKeyboardMarkup
from telebot.types import KeyboardButton


from telegram.generators.generator import generate
from telegram.ui.main import ui as main


greetings = {
    'number_min': 'Укажите минимальное значение',
    'number_max': 'Укажите максимальное заничание',
    'number_count': 'Укажите количество',
    'number_separator': 'Укажите разделитель',
    'number_repeat': 'Повторять значения?'
}


menus = {
    'number_min': ['0', '1', '10', 'Просто сделай это', 'Меню'],
    'number_max': ['10', '100', '1000', 'Просто сделай это', 'Меню'],
    'number_count': ['1', '10', '100', 'Просто сделай это', 'Меню'],
    'number_separator': ['Запятая', 'Пробел', 'Запятая с пробелом', 'Просто сделай это', 'Меню'],
    'number_repeat': ['Да', 'Нет', 'Просто сделай это', 'Меню']
}


def dispatch(bot, chats, chat_id, command):
    key_board = ReplyKeyboardMarkup()
    command = command.strip()
    chat = chats.get(chat_id) if chats.get(chat_id) is not None else {}
    if command == 'Числа' or command == 'numbers':
        chat['processor'] = 'numbers'
        key_board.add(*map(lambda text: KeyboardButton(text), menus.get('number_min')))
        bot.send_message(chat_id=chat_id, text=greetings.get('number_min'), reply_markup=key_board)
        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'numbers' and chat.get('min') is None:
        chat['min'] = command
        key_board.add(*map(lambda text: KeyboardButton(text), menus.get('number_max')))
        bot.send_message(chat_id=chat_id, text=greetings.get('number_max'), reply_markup=key_board)
        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'numbers' and chat.get('max') is None:
        chat['max'] = command
        key_board.add(*map(lambda text: KeyboardButton(text), menus.get('number_count')))
        bot.send_message(chat_id=chat_id, text=greetings.get('number_count'), reply_markup=key_board)
        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'numbers' and chat.get('count') is None:
        chat['count'] = command
        key_board.add(*map(lambda text: KeyboardButton(text), menus.get('number_separator')))
        bot.send_message(chat_id=chat_id, text=greetings.get('number_separator'), reply_markup=key_board)
        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'numbers' and chat.get('separator') is None:
        if command == 'Пробел':
            command = 'space'
        elif command == 'Запятая':
            command = 'comma'
        elif command == 'Запятая с пробелом':
            command = 'spacecomma'
        chat['separator'] = command
        key_board.add(*map(lambda text: KeyboardButton(text), menus.get('number_repeat')))
        bot.send_message(chat_id=chat_id, text=greetings.get('number_repeat'), reply_markup=key_board)
        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'numbers' and chat.get('repeat') is None:
        if command == 'Да':
            command = '0'
        elif command == 'Нет':
            command = '1'
        chat['repeat'] = command
        key_board.add(*map(lambda text: KeyboardButton(text), main.menus.get('main')))
        bot.send_message(chat_id=chat_id, text=generate(chat), reply_markup=key_board)
        del chats[chat_id]
        return True
    return False
