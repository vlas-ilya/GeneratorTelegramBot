# -*- coding: utf-8 -*-


from telebot.types import ReplyKeyboardMarkup
from telebot.types import KeyboardButton


from telegram.generators.generator import generate
from telegram.ui.main import ui as main


greetings = {
    'inn_type': 'Выберите тип ИНН/ОГРН/КПП',
    'inn_start': 'Если необходимо, введите начало ИНН/ОГРН/КПП, и генератор его дополнит или исправит',
}


menus = {
    'inn_type': ['ИНН_ЮЛ', 'ИНН_ИП', 'ОГРН_ЮЛ', 'ОГРН_ИП', 'UUID', 'uuid', 'Меню'],
    'inn_start': ['Просто сделай это', 'Меню'],
}


def dispatch(bot, chats, chat_id, command):
    key_board = ReplyKeyboardMarkup()
    command = command.strip()
    chat = chats.get(chat_id) if chats.get(chat_id) is not None else {}
    if command.upper() == 'ИНН/ОГРН/UUID' or command.upper() == 'INN':
        chat['processor'] = 'inn'
        key_board.add(*map(lambda text: KeyboardButton(text), menus.get('inn_type')))
        bot.send_message(chat_id=chat_id, text=greetings.get('inn_type'), reply_markup=key_board)
        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'inn' and chat.get('type') is None:
        chat["type"] = command
        key_board.add(*map(lambda text: KeyboardButton(text), menus.get('inn_start')))
        bot.send_message(chat_id=chat_id, text=greetings.get('inn_start'), reply_markup=key_board)
        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'inn' and chat.get('type') is not None:
        if chat["type"] == "ЮЛ" and len(command) > 8:
            command = command[:8]
        elif len(command) > 10:
            command = command[:10]
        chat['inn'] = command
        chats[chat_id] = chat
        key_board.add(*map(lambda text: KeyboardButton(text), main.menus.get('main')))
        bot.send_message(chat_id=chat_id, text=generate(chat), reply_markup=key_board)
        del chats[chat_id]
        return True
    return False
