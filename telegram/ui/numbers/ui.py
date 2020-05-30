# -*- coding: utf-8 -*-


from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton


from telegram.generators.generator import generate
from telegram.ui.main import ui as main


greetings = {
    'number_min': 'Укажите минимальное значение',
    'number_max': 'Укажите максимальное заничание',
    'number_count': 'Укажите количество',
    'number_separator': 'Укажите разделитель',
    'number_repeat': 'Повторять значения?'
}


buttons = {
    'number_min': [
        InlineKeyboardButton(text='0', callback_data='0'),
        InlineKeyboardButton(text='1', callback_data='1'),
        InlineKeyboardButton(text='10', callback_data='10'),
        InlineKeyboardButton(text='Просто сделай это', callback_data='Просто сделай это')
    ],
    'number_max': [
        InlineKeyboardButton(text='10', callback_data='10'),
        InlineKeyboardButton(text='100', callback_data='100'),
        InlineKeyboardButton(text='1000', callback_data='1000'),
        InlineKeyboardButton(text='Просто сделай это', callback_data='Просто сделай это')
    ],
    'number_count': [
        InlineKeyboardButton(text='1', callback_data='1'),
        InlineKeyboardButton(text='10', callback_data='10'),
        InlineKeyboardButton(text='100', callback_data='100'),
        InlineKeyboardButton(text='Просто сделай это', callback_data='Просто сделай это')
    ],
    'number_separator': [
        InlineKeyboardButton(text='Запятая', callback_data='Запятая'),
        InlineKeyboardButton(text='Пробел', callback_data='Пробел'),
        InlineKeyboardButton(text='Запятая с пробелом', callback_data='Запятая с пробелом'),
        InlineKeyboardButton(text='Просто сделай это', callback_data='Просто сделай это')
    ],
    'number_repeat': [
        InlineKeyboardButton(text='Да', callback_data='Да'),
        InlineKeyboardButton(text='Нет',  callback_data='Нет'),
        InlineKeyboardButton(text='Просто сделай это', callback_data='Просто сделай это')
    ]
}


def dispatch(bot, chats, chat_id, command, message_id):

    command = command.strip()
    chat = chats.get(chat_id) if chats.get(chat_id) is not None else {}

    if command == 'Числа' or command == 'numbers':
        chat['processor'] = 'numbers'

        key_board = InlineKeyboardMarkup(row_width=3)
        key_board.add(*buttons.get('number_min'))

        chat['message_id'] = message_id

        bot.edit_message_text(chat_id=chat_id,
                              message_id=message_id,
                              text=greetings.get('number_min'),
                              reply_markup=key_board)

        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'numbers' and chat.get('min') is None:
        chat['min'] = command

        key_board = InlineKeyboardMarkup(row_width=3)
        key_board.add(*buttons.get('number_max'))

        if message_id is None:
            message_id = chat['message_id']
        chat['message_id'] = message_id

        bot.edit_message_text(chat_id=chat_id,
                              message_id=message_id,
                              text=greetings.get('number_max'),
                              reply_markup=key_board)

        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'numbers' and chat.get('max') is None:
        chat['max'] = command

        key_board = InlineKeyboardMarkup(row_width=3)
        key_board.add(*buttons.get('number_count'))

        if message_id is None:
            message_id = chat['message_id']
        chat['message_id'] = message_id

        bot.edit_message_text(chat_id=chat_id,
                              message_id=message_id,
                              text=greetings.get('number_count'),
                              reply_markup=key_board)

        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'numbers' and chat.get('count') is None:
        chat['count'] = command

        key_board = InlineKeyboardMarkup(row_width=3)
        key_board.add(*buttons.get('number_separator'))

        if message_id is None:
            message_id = chat['message_id']
        chat['message_id'] = message_id

        bot.edit_message_text(chat_id=chat_id,
                              message_id=message_id,
                              text=greetings.get('number_separator'),
                              reply_markup=key_board)

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

        key_board = InlineKeyboardMarkup(row_width=3)
        key_board.add(*buttons.get('number_repeat'))

        if message_id is None:
            message_id = chat['message_id']
        chat['message_id'] = message_id

        bot.edit_message_text(chat_id=chat_id,
                              message_id=message_id,
                              text=greetings.get('number_repeat'),
                              reply_markup=key_board)

        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'numbers' and chat.get('repeat') is None:
        if command == 'Да':
            command = '0'
        elif command == 'Нет':
            command = '1'
        chat['repeat'] = command

        key_board = InlineKeyboardMarkup(row_width=1)
        key_board.add(*main.buttons.get('end'))

        if message_id is None:
            message_id = chat['message_id']
        chat['message_id'] = message_id

        if chat.get('message_id') is not None:
            del chat['message_id']

        bot.edit_message_text(chat_id=chat_id,
                              message_id=message_id,
                              text='\n\n' + generate(chat) + '\n\n' + main.greetings['end'],
                              reply_markup=key_board)

        del chats[chat_id]
        return True
    return False
