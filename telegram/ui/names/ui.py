# -*- coding: utf-8 -*-


from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton


from telegram.generators.generator import generate
from telegram.ui.main import ui as main


greetings = {
    'names_sex': 'Выберите пол',
    'names_field': 'Выберите необходимые поля',
    'names_count': 'Выберите количество имен'
}


buttons = {
    'names_sex': [
        InlineKeyboardButton(text='М', callback_data='man'),
        InlineKeyboardButton(text='Ж', callback_data='woman'),
        InlineKeyboardButton(text='Все ровно', callback_data='all'),
        InlineKeyboardButton(text='Nicknames', callback_data='nick'),
        InlineKeyboardButton(text='Просто сделай это', callback_data='Просто сделай это')
    ],
    'names_field': [
        InlineKeyboardButton(text='ФИО', callback_data='ФИО'),
        InlineKeyboardButton(text='Ф', callback_data='Ф'),
        InlineKeyboardButton(text='И', callback_data='И'),
        InlineKeyboardButton(text='О', callback_data='О'),
        InlineKeyboardButton(text='ФИ', callback_data='ФИ'),
        InlineKeyboardButton(text='ИО', callback_data='ИО'),
        InlineKeyboardButton(text='Просто сделай это', callback_data='Просто сделай это')
    ],
    'names_count': [
        InlineKeyboardButton(text='1', callback_data='1'),
        InlineKeyboardButton(text='10', callback_data='10'),
        InlineKeyboardButton(text='100', callback_data='100'),
        InlineKeyboardButton(text='Просто сделай это', callback_data='Просто сделай это')
    ]
}


def dispatch(bot, chats, chat_id, command, message_id):

    command = command.strip()
    chat = chats.get(chat_id) if chats.get(chat_id) is not None else {}

    if command == 'Имена':
        chat['processor'] = 'names'

        key_board = InlineKeyboardMarkup(row_width=3)
        key_board.add(*buttons.get('names_sex'))

        bot.edit_message_text(chat_id=chat_id,
                              message_id=message_id,
                              text=greetings.get('names_sex'),
                              reply_markup=key_board)

        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'names' and chat.get('sex') is None:
        chat['sex'] = command

        if command == 'nick':
            key_board = InlineKeyboardMarkup(row_width=3)
            key_board.add(*buttons.get('names_count'))

            bot.edit_message_text(chat_id=chat_id,
                                  message_id=message_id,
                                  text=greetings.get('names_count'),
                                  reply_markup=key_board)
        else:
            key_board = InlineKeyboardMarkup(row_width=3)
            key_board.add(*buttons.get('names_field'))

            bot.edit_message_text(chat_id=chat_id,
                                  message_id=message_id,
                                  text=greetings.get('names_field'),
                                  reply_markup=key_board)

        chat['message_id'] = message_id
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

        key_board = InlineKeyboardMarkup(row_width=3)
        key_board.add(*buttons.get('names_count'))

        bot.edit_message_text(chat_id=chat_id,
                              message_id=message_id,
                              text=greetings.get('names_count'),
                              reply_markup=key_board)

        return True
    elif chat.get('processor') == 'names' and chat.get('count') is None:
        chat['count'] = command
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
