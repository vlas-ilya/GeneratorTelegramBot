# -*- coding: utf-8 -*-


from telebot.types import ReplyKeyboardMarkup
from telebot.types import KeyboardButton
from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton


from src.generators.generator import generate


greetings = {
    'start': 'GeneratorsBot - это набор наиболее часто используемых генераторов для различных задач.',
    'main': 'Выберите генератор',
    'error': "Что-то пошло не так",
    'help': "пожалуйста, оцените бота тут: https://storebot.me/bot/gen_ru_bot",
    'end': "Спасибо, что пользуетесь ботом!"
}

buttons = {
    'start': [
        KeyboardButton('Поехали')
    ],
    'main': [
        [
            InlineKeyboardButton(text='Текст', callback_data='Текст'),
            InlineKeyboardButton(text='Числа', callback_data='Числа'),
            InlineKeyboardButton(text='Имена', callback_data='Имена')
        ], [
            InlineKeyboardButton(text='Шутки', callback_data='Шутки'),
            InlineKeyboardButton(text='Комплименты', callback_data='Комплименты'),
            InlineKeyboardButton(text='Пароли', callback_data='Пароли')
        ], [
            InlineKeyboardButton(text='Цитаты', callback_data='Цитаты'),
            InlineKeyboardButton(text='Факты', callback_data='Факты'),
            InlineKeyboardButton(text='ИНН/ОГРН/UUID', callback_data='ИНН/ОГРН/UUID')
        ]
    ],
    'end': [
        InlineKeyboardButton(text='Поделиться в VK', url='https://vk.com/share.php?url=https://telegram.me/gen_ru_bot?'),
        InlineKeyboardButton(text='Поделиться в Facebook', url='https://www.facebook.com/sharer.php?u=https://telegram.me/gen_ru_bot?'),
        InlineKeyboardButton(text='Поделиться в Twitter', url='https://twitter.com/intent/tweet?text=GeneratorsBot%20-%20это%20набор%20наиболее%20часто%20используемых%20генераторов%20для%20различных%20задач.%20https://telegram.me/gen_ru_bot&original_referer=?'),
        InlineKeyboardButton(text='Сгенерировать еще', callback_data='Поехали')
    ]
}


def dispatch(bot, chats, chat_id, command, message_id):

    command = command.strip()

    if command.startswith('/start') or command == 'Поехали' or command == 'Меню':
        chats[chat_id] = {}

        key_board = ReplyKeyboardMarkup()
        key_board.add(*buttons.get('start'))
        bot.send_message(chat_id=chat_id, text=greetings.get('start'), reply_markup=key_board)

        key_board = InlineKeyboardMarkup(row_width=3)
        key_board.add(*buttons.get('main')[0]),
        key_board.add(*buttons.get('main')[1]),
        key_board.add(*buttons.get('main')[2]),

        bot.send_message(chat_id=chat_id, text=greetings.get('main'), reply_markup=key_board)

        return True
    elif command == 'Просто сделай это':
        chat = chats.get(chat_id) if chats.get(chat_id) is not None else {}

        key_board = InlineKeyboardMarkup(row_width=1)
        key_board.add(*buttons.get('end'))

        if chat.get('message_id') is not None:
            del chat['message_id']

        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text='\n\n' + generate(chat) + '\n\n' + greetings['end'],
            reply_markup=key_board
        )

        del chats[chat_id]

        return True
    return False
