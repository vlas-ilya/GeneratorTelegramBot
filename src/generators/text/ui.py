# -*- coding: utf-8 -*-


from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton


from src.generators.generator import generate
from src.generators import ui as main

greetings = {
    'text_type': "Выберите тематику текста",
    'text_paragraph': 'Укажите число параграфов в тексте',
    'text_words': 'Укажите число слов в параграфе'
}


buttons = {
    'text_type': [
        InlineKeyboardButton(text='Классическая проза', callback_data='Классическая проза'),
        InlineKeyboardButton(text='Бизнес и финансы', callback_data='Бизнес и финансы'),
        InlineKeyboardButton(text='Юмор и развлечения', callback_data='Юмор и развлечения'),
        InlineKeyboardButton(text='Дом и семья', callback_data='Дом и семья'),
        InlineKeyboardButton(text='Медицина и здоровье', callback_data='Медицина и здоровье'),
        InlineKeyboardButton(text='Lorem Ipsum', callback_data='Lorem Ipsum'),
        InlineKeyboardButton(text='О рыбе...', callback_data='О рыбе...'),
        InlineKeyboardButton(text='Просто сделай это', callback_data='Просто сделай это'),
    ],
    'text_paragraph': [
        InlineKeyboardButton(text='1', callback_data='1'),
        InlineKeyboardButton(text='3', callback_data='3'),
        InlineKeyboardButton(text='9', callback_data='9'),
        InlineKeyboardButton(text='Просто сделай это', callback_data='Просто сделай это'),
    ],
    'text_words': [
        InlineKeyboardButton(text='10', callback_data='10'),
        InlineKeyboardButton(text='50', callback_data='50'),
        InlineKeyboardButton(text='100', callback_data='100'),
        InlineKeyboardButton(text='Просто сделай это', callback_data='Просто сделай это'),
    ]
}


def dispatch(bot, chats, chat_id, command, message_id):

    command = command.strip()
    chat = chats.get(chat_id) if chats.get(chat_id) is not None else {}

    if command == 'Текст' or command == 'text':
        chat['processor'] = 'text'

        key_board = InlineKeyboardMarkup(row_width=3)
        key_board.add(*buttons.get('text_type'))

        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=greetings.get('text_type'),
            reply_markup=key_board
        )

        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'text' and (command == 'Классическая проза' or command == 'prose'):
        chat['type'] = 'prose'

        key_board = InlineKeyboardMarkup(row_width=3)
        key_board.add(*buttons.get('text_paragraph'))

        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=greetings.get('text_paragraph'),
            reply_markup=key_board
        )

        chat['message_id'] = message_id
        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'text' and (command == 'Бизнес и финансы' or command == 'business'):
        chat['type'] = 'business'

        key_board = InlineKeyboardMarkup(row_width=3)
        key_board.add(*buttons.get('text_paragraph'))

        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=greetings.get('text_paragraph'),
            reply_markup=key_board
        )

        chat['message_id'] = message_id
        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'text' and (command == 'Наука и техника' or command == 'science'):
        chat['type'] = 'science'

        key_board = InlineKeyboardMarkup(row_width=3)
        key_board.add(*buttons.get('text_paragraph'))

        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=greetings.get('text_paragraph'),
            reply_markup=key_board
        )

        chat['message_id'] = message_id
        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'text' and (command == 'Юмор и развлечения' or command == 'humor'):
        chat['type'] = 'humor'

        key_board = InlineKeyboardMarkup(row_width=3)
        key_board.add(*buttons.get('text_paragraph'))

        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=greetings.get('text_paragraph'),
            reply_markup=key_board
        )

        chat['message_id'] = message_id
        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'text' and (command == 'Дом и семья' or command == 'home'):
        chat['type'] = 'home'

        key_board = InlineKeyboardMarkup(row_width=3)
        key_board.add(*buttons.get('text_paragraph'))

        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=greetings.get('text_paragraph'),
            reply_markup=key_board
        )

        chat['message_id'] = message_id
        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'text' and (command == 'Медицина и здоровье' or command == 'med'):
        chat['type'] = 'med'

        key_board = InlineKeyboardMarkup(row_width=3)
        key_board.add(*buttons.get('text_paragraph'))

        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=greetings.get('text_paragraph'),
            reply_markup=key_board
        )

        chat['message_id'] = message_id
        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'text' and (command == 'Lorem Ipsum' or command == 'lorem'):
        chat['type'] = 'lorem'

        key_board = InlineKeyboardMarkup(row_width=3)
        key_board.add(*buttons.get('text_paragraph'))

        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=greetings.get('text_paragraph'),
            reply_markup=key_board
        )

        chat['message_id'] = message_id
        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'text' and (command == 'О рыбе...' or command == 'fish'):
        chat['type'] = 'fish'

        key_board = InlineKeyboardMarkup(row_width=3)
        key_board.add(*buttons.get('text_paragraph'))

        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=greetings.get('text_paragraph'),
            reply_markup=key_board
        )

        chat['message_id'] = message_id
        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'text' and chat.get("type") is not None and chat.get('paragraph') is None:
        chat['paragraph'] = command

        key_board = InlineKeyboardMarkup(row_width=3)
        key_board.add(*buttons.get('text_words'))

        if message_id is None:
            message_id = chat['message_id']
        chat['message_id'] = message_id

        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=greetings.get('text_words'),
            reply_markup=key_board
        )

        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'text' and chat.get("type") is not None and chat.get('paragraph') is not None:
        chat['word'] = command

        key_board = InlineKeyboardMarkup(row_width=1)
        key_board.add(*main.buttons.get('end'))

        if message_id is None:
            message_id = chat['message_id']

        if chat.get('message_id') is not None:
            del chat['message_id']

        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text='\n\n' + generate(chat) + '\n\n' + main.greetings['end'],
            reply_markup=key_board
        )

        del chats[chat_id]
        return True
    return False
