# -*- coding: utf-8 -*-


from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton


from telegram.generators.generator import generate
from telegram.ui.main import ui as main


greetings = {
    'inn_type': 'Выберите тип ИНН/ОГРН/КПП',
    'inn_start': 'Если необходимо, введите начало ИНН/ОГРН/КПП, и генератор его дополнит или исправит',
    'uuid_start': 'Введите количество',
}


buttons = {
    'inn_type': [
        InlineKeyboardButton(text='ИНН ЮЛ', callback_data='ИНН_ЮЛ'),
        InlineKeyboardButton(text='ИНН ИП', callback_data='ИНН_ИП'),
        InlineKeyboardButton(text='ОГРН ЮЛ', callback_data='ОГРН_ЮЛ'),
        InlineKeyboardButton(text='ОГРН ИП', callback_data='ОГРН_ИП'),
        InlineKeyboardButton(text='UUID', callback_data='UUID'),
        InlineKeyboardButton(text='uuid', callback_data='uuid'),
    ],
    'inn_start': [
        InlineKeyboardButton(text='Просто сделай это', callback_data='Просто сделай это')
    ],
    'uuid_start': [
        InlineKeyboardButton(text='1', callback_data='1'),
        InlineKeyboardButton(text='5', callback_data='5'),
        InlineKeyboardButton(text='10', callback_data='10'),
        InlineKeyboardButton(text='20', callback_data='20'),
        InlineKeyboardButton(text='100', callback_data='100'),
    ],
}


def dispatch(bot, chats, chat_id, command, message_id):

    command = command.strip()
    chat = chats.get(chat_id) if chats.get(chat_id) is not None else {}

    if command.upper() == 'ИНН/ОГРН/UUID' or command.upper() == 'INN':
        chat['processor'] = 'inn'

        key_board = InlineKeyboardMarkup(row_width=3)
        key_board.add(*buttons.get('inn_type'))

        bot.edit_message_text(chat_id=chat_id,
                              message_id=message_id,
                              text=greetings.get('inn_type'),
                              reply_markup=key_board)

        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'inn' and chat.get('type') is None and (command == 'uuid' or command == 'UUID'):
        chat["type"] = command

        key_board = InlineKeyboardMarkup(row_width=3)
        key_board.add(*buttons.get('uuid_start'))

        bot.edit_message_text(chat_id=chat_id,
                              message_id=message_id,
                              text=greetings.get('uuid_start'),
                              reply_markup=key_board)

        chat['message_id'] = message_id

        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'inn' and chat.get('type') is None:
        chat["type"] = command

        key_board = InlineKeyboardMarkup(row_width=3)
        key_board.add(*buttons.get('inn_start'))

        bot.edit_message_text(chat_id=chat_id,
                              message_id=message_id,
                              text=greetings.get('inn_start'),
                              reply_markup=key_board)

        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'inn' and chat.get('type') is not None:
        chat['inn'] = command
        chats[chat_id] = chat

        key_board = InlineKeyboardMarkup(row_width=1)
        key_board.add(*main.buttons.get('end'))

        if message_id is None:
            message_id = chat['message_id']

        if chat.get('message_id') is not None:
            del chat['message_id']

        bot.edit_message_text(chat_id=chat_id,
                              message_id=message_id,
                              text='\n\n' + generate(chat) + '\n\n' + main.greetings['end'],
                              reply_markup=key_board)

        del chats[chat_id]
        return True
    return False
