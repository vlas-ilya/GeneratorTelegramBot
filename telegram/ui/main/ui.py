# -*- coding: utf-8 -*-


from telebot.types import ReplyKeyboardMarkup
from telebot.types import KeyboardButton


from telegram.generators.generator import generate


greetings = {
    'main': "GeneratorsBot - это набор наиболее часто используемых генераторов для различных задач."
            "\n\nВыберите генератор:",
    'error': "Что-то пошло не так",
    'help': "пожалуйста, оцените бота тут: https://storebot.me/bot/gen_ru_bot"
}


menus = {
    'main': ['Текст', 'Числа', 'Имена', 'Шутки', 'Комплименты', 'Пароли', 'Цитаты', 'Факты', 'Инн', 'Помощь']
}


def dispatch(bot, chats, chat_id, command):
    key_board = ReplyKeyboardMarkup()
    command = command.strip()
    if command.startswith('/start') or command == 'menu' or command == '/menu' or command == 'Меню':
        chats[chat_id] = {}
        key_board.add(*map(lambda text: KeyboardButton(text), menus.get('main')))
        bot.send_message(chat_id=chat_id, text=greetings.get('main'), reply_markup=key_board)
        return True
    elif command == 'Просто сделай это':
        chat = chats.get(chat_id) if chats.get(chat_id) is not None else {}
        key_board.add(*map(lambda text: KeyboardButton(text), menus.get('main')))
        bot.send_message(chat_id=chat_id, text=generate(chat), reply_markup=key_board)
        del chats[chat_id]
        return True
    if command == 'Помощь' or command == 'help':
        key_board.add(*map(lambda text: KeyboardButton(text), menus.get('main')))
        bot.send_message(chat_id=chat_id, text=greetings.get('help'), reply_markup=key_board)
        return True
    return False
