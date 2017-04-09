# -*- coding: utf-8 -*-

from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton


from telegram.generators.generator import generate
from telegram.ui.main import ui as main


greetings = {
    'compliments_sex': 'Выберите пол',
    'compliments_type': 'Выберите тип'
}


buttons = {
    'compliments_sex': [
        InlineKeyboardButton(text='М', callback_data='man'),
        InlineKeyboardButton(text='Ж', callback_data='woman'),
        InlineKeyboardButton(text='Все ровно', callback_data='all'),
        InlineKeyboardButton(text='Просто сделай это', callback_data='Просто сделай это')
    ],
    'compliments_type': [
        InlineKeyboardButton(text='Слово', callback_data='1'),
        InlineKeyboardButton(text='Фраза', callback_data='0'),
        InlineKeyboardButton(text='Просто сделай это', callback_data='Просто сделай это')
    ]
}



def dispatch(bot, chats, chat_id, command, message_id):

    command = command.strip()
    chat = chats.get(chat_id) if chats.get(chat_id) is not None else {}

    if command == 'Комплименты':
        chat['processor'] = 'compliments'

        key_board = InlineKeyboardMarkup(row_width=3)
        key_board.add(*buttons.get('compliments_sex'))

        bot.edit_message_text(chat_id=chat_id,
                              message_id=message_id,
                              text=greetings.get('compliments_sex'),
                              reply_markup=key_board)

        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'compliments' and chat.get('sex') is None:
        chat['sex'] = command

        key_board = InlineKeyboardMarkup(row_width=3)
        key_board.add(*buttons.get('compliments_type'))

        bot.edit_message_text(chat_id=chat_id,
                              message_id=message_id,
                              text=greetings.get('compliments_type'),
                              reply_markup=key_board)

        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'compliments' and chat.get('type_compl') is None:
        chat['type_compl'] = command
        chats[chat_id] = chat

        key_board = InlineKeyboardMarkup(row_width=1)
        key_board.add(*main.buttons.get('end'))
        bot.edit_message_text(chat_id=chat_id,
                              message_id=message_id,
                              text='\n\n' + generate(chat) + '\n\n' + main.greetings['end'],
                              reply_markup=key_board)

        del chats[chat_id]
        return True
    return False
