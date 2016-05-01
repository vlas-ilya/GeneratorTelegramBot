# -*- coding: utf-8 -*-


from telebot.types import ReplyKeyboardMarkup
from telebot.types import KeyboardButton


from telegram.generators.generator import generate
from telegram.ui.main import ui as main


greetings = {
    'compliments_sex': 'Выберите пол',
    'compliments_type': 'Выберите тип'
}


menus = {
    'compliments_sex': ['М', 'Ж', 'Все ровно', 'Просто сделай это', 'Меню'],
    'compliments_type': ['Слово', 'Фраза', 'Просто сделай это', 'Меню']
}


def dispatch(bot, chats, chat_id, command):
    key_board = ReplyKeyboardMarkup()
    command = command.strip()
    chat = chats.get(chat_id) if chats.get(chat_id) is not None else {}
    if command == 'Комплименты' or command == 'compliments':
        chat['processor'] = 'compliments'
        key_board.add(*map(lambda text: KeyboardButton(text), menus.get('compliments_sex')))
        bot.send_message(chat_id=chat_id, text=greetings.get('compliments_sex'), reply_markup=key_board)
        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'compliments' and chat.get('sex') is None:
        if command == 'М':
            command = 'man'
        elif command == 'Ж':
            command = 'woman'
        elif command == 'Все ровно':
            command = 'all'
        chat['sex'] = command
        key_board.add(*map(lambda text: KeyboardButton(text), menus.get('compliments_type')))
        bot.send_message(chat_id=chat_id, text=greetings.get('compliments_type'), reply_markup=key_board)
        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'compliments' and chat.get('type_compl') is None:
        if command == 'Фраза':
            command = '0'
        elif command == 'Слово':
            command = '1'
        chat['type_compl'] = command
        chats[chat_id] = chat
        key_board.add(*map(lambda text: KeyboardButton(text), main.menus.get('main')))
        bot.send_message(chat_id=chat_id, text=generate(chat), reply_markup=key_board)
        del chats[chat_id]
        return True
    return False
