# -*- coding: utf-8 -*-


from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton


from telegram.generators.generator import generate
from telegram.ui.main import ui as main


greetings = {
    'passwords_count': 'Выберите колличество символов в пароле',
    'passwords_type': 'Выберите состав символов в пароле'
}


buttons = {
    'passwords_count': [
        InlineKeyboardButton(text='6', callback_data='6'),
        InlineKeyboardButton(text='10', callback_data='10'),
        InlineKeyboardButton(text='14', callback_data='14'),
        InlineKeyboardButton(text='Просто сделай это', callback_data='Просто сделай это')
    ],
    'passwords_type': [
        InlineKeyboardButton(text='Буквы и Цифры', callback_data='Буквы и Цифры'),
        InlineKeyboardButton(text='Буквы', callback_data='Буквы'),
        InlineKeyboardButton(text='Буквы, Цифры и Символы', callback_data='Буквы, Цифры и Символы'),
        InlineKeyboardButton(text='Просто сделай это', callback_data='Просто сделай это'),
    ]
}


def dispatch(bot, chats, chat_id, command, message_id):

    command = command.strip()
    chat = chats.get(chat_id) if chats.get(chat_id) is not None else {}

    if command == 'Пароли':
        chat['processor'] = 'passwords'

        key_board = InlineKeyboardMarkup(row_width=3)
        key_board.add(*buttons.get('passwords_count'))

        bot.edit_message_text(chat_id=chat_id,
                              message_id=message_id,
                              text=greetings.get('passwords_count'),
                              reply_markup=key_board)

        chat['message_id'] = message_id
        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'passwords' and chat.get('count') is None:
        chat['count'] = str(command)

        key_board = InlineKeyboardMarkup(row_width=3)
        key_board.add(*buttons.get('passwords_type'))

        if message_id is None:
            message_id = chat['message_id']

        bot.edit_message_text(chat_id=chat_id,
                              message_id=message_id,
                              text=greetings.get('passwords_type'),
                              reply_markup=key_board)

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

        key_board = InlineKeyboardMarkup(row_width=1)
        key_board.add(*main.buttons.get('end'))

        if chat.get('message_id') is not None:
            del chat['message_id']

        bot.edit_message_text(chat_id=chat_id,
                              message_id=message_id,
                              text='\n\n' + generate(chat) + '\n\n' + main.greetings['end'],
                              reply_markup=key_board)

        del chats[chat_id]
        return True
    return False
