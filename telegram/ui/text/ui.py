# -*- coding: utf-8 -*-


from telebot.types import ReplyKeyboardMarkup
from telebot.types import KeyboardButton


from telegram.generators.generator import generate
from telegram.ui.main import ui as main


greetings = {
    'text_type': "Выберите тематику текста",
    'text_paragraph': 'Укажите число параграфов в тексте',
    'text_words': 'Укажите число слов в параграфе'
}


menus = {
    'text_type': ['Классическая проза', 'Бизнес и финансы', 'Юмор и развлечения', 'Дом и семья',
                  'Медицина и здоровье', 'Lorem Ipsum', 'О рыбе...', 'Просто сделай это', 'Меню'],
    'text_paragraph': ['1', '3', '9', 'Просто сделай это', 'Меню'],
    'text_words': ['10', '50', '100', 'Просто сделай это', 'Меню']
}


def dispatch(bot, chats, chat_id, command):
    key_board = ReplyKeyboardMarkup()
    command = command.strip()
    chat = chats.get(chat_id) if chats.get(chat_id) is not None else {}
    if command == 'Текст' or command == 'text':
        chat['processor'] = 'text'
        key_board.add(*map(lambda text: KeyboardButton(text), menus.get('text_type')))
        bot.send_message(chat_id=chat_id, text=greetings.get('text_type'), reply_markup=key_board)
        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'text' and (command == 'Классическая проза' or command == 'prose'):
        chat['type'] = 'prose'
        key_board.add(*map(lambda text: KeyboardButton(text), menus.get('text_paragraph')))
        bot.send_message(chat_id=chat_id, text=greetings.get('text_paragraph'), reply_markup=key_board)
        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'text' and (command == 'Бизнес и финансы' or command == 'business'):
        chat['type'] = 'business'
        key_board.add(*map(lambda text: KeyboardButton(text), menus.get('text_paragraph')))
        bot.send_message(chat_id=chat_id, text=greetings.get('text_paragraph'), reply_markup=key_board)
        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'text' and (command == 'Наука и техника' or command == 'science'):
        chat['type'] = 'science'
        key_board.add(*map(lambda text: KeyboardButton(text), menus.get('text_paragraph')))
        bot.send_message(chat_id=chat_id, text=greetings.get('text_paragraph'), reply_markup=key_board)
        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'text' and (command == 'Юмор и развлечения' or command == 'humor'):
        chat['type'] = 'humor'
        key_board.add(*map(lambda text: KeyboardButton(text), menus.get('text_paragraph')))
        bot.send_message(chat_id=chat_id, text=greetings.get('text_paragraph'), reply_markup=key_board)
        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'text' and (command == 'Дом и семья' or command == 'home'):
        chat['type'] = 'home'
        key_board.add(*map(lambda text: KeyboardButton(text), menus.get('text_paragraph')))
        bot.send_message(chat_id=chat_id, text=greetings.get('text_paragraph'), reply_markup=key_board)
        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'text' and (command == 'Медицина и здоровье' or command == 'med'):
        chat['type'] = 'med'
        key_board.add(*map(lambda text: KeyboardButton(text), menus.get('text_paragraph')))
        bot.send_message(chat_id=chat_id, text=greetings.get('text_paragraph'), reply_markup=key_board)
        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'text' and (command == 'Lorem Ipsum' or command == 'lorem'):
        chat['type'] = 'lorem'
        key_board.add(*map(lambda text: KeyboardButton(text), menus.get('text_paragraph')))
        bot.send_message(chat_id=chat_id, text=greetings.get('text_paragraph'), reply_markup=key_board)
        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'text' and (command == 'О рыбе...' or command == 'fish'):
        chat['type'] = 'fish'
        key_board.add(*map(lambda text: KeyboardButton(text), menus.get('text_paragraph')))
        bot.send_message(chat_id=chat_id, text=greetings.get('text_paragraph'), reply_markup=key_board)
        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'text' and chat.get("type") is not None and chat.get('paragraph') is None:
        chat['paragraph'] = command
        key_board.add(*map(lambda text: KeyboardButton(text), menus.get('text_words')))
        bot.send_message(chat_id=chat_id, text=greetings.get('text_words'), reply_markup=key_board)
        chats[chat_id] = chat
        return True
    elif chat.get('processor') == 'text' and chat.get("type") is not None and chat.get('paragraph') is not None:
        chat['word'] = command
        key_board.add(*map(lambda text: KeyboardButton(text), main.menus.get('main')))
        bot.send_message(chat_id=chat_id, text=generate(chat), reply_markup=key_board)
        del chats[chat_id]
        return True
    return False
