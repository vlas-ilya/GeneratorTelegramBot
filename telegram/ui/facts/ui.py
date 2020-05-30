# -*- coding: utf-8 -*-


from telebot.types import InlineKeyboardMarkup


from telegram.generators.generator import generate
from telegram.ui.main import ui as main


def dispatch(bot, chats, chat_id, command, message_id):

    command = command.strip()
    chat = chats.get(chat_id) if chats.get(chat_id) is not None else {}

    if command == 'Факты' or command == 'facts':
        chat['processor'] = 'facts'
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
