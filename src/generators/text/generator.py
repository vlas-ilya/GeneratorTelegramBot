# -*- coding: utf-8 -*-


from src.generators.text import dao

generators = {
    "prose": lambda: dao.get_random_text_prose(),
    "business": lambda: dao.get_random_text_business(),
    "science": lambda: dao.get_random_text_science(),
    "humor": lambda: dao.get_random_text_humor(),
    "home": lambda: dao.get_random_text_home(),
    "med": lambda: dao.get_random_text_med(),
    "lorem": lambda: dao.get_random_text_lorem(),
    "fish": lambda: dao.get_random_text_fish()
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
