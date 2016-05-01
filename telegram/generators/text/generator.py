# -*- coding: utf-8 -*-


from telegram.dao import text_dao


generators = {
    "prose": lambda: text_dao.get_random_text_prose(),
    "business": lambda: text_dao.get_random_text_business(),
    "science": lambda: text_dao.get_random_text_science(),
    "humor": lambda: text_dao.get_random_text_humor(),
    "home": lambda: text_dao.get_random_text_home(),
    "med": lambda: text_dao.get_random_text_med(),
    "lorem": lambda: text_dao.get_random_text_lorem(),
    "fish": lambda: text_dao.get_random_text_fish()
}


def _generate_paragraph(generator, words_count):
    result = ""
    while len(result.split(" ")) < words_count:
        result += generator() + ". "
    return result


def generate(params):
    paragraph = int(params.paragraph)
    word_count = int(params.word)
    generator = generators[params.type]
    return "\n\n".join([_generate_paragraph(generator, word_count) for _ in range(0, paragraph)])
