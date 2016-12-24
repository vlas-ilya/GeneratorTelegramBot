# -*- coding: utf-8 -*-


import random
import uuid


def _generate_inn_for_juridical_person(start_inn):
    multipliers = [2, 4, 10, 3, 5, 9, 4, 6, 8]
    N10 = 0
    result = ""
    for i in range(0, 9):
        n = int(start_inn[i]) if len(start_inn) > i else random.randint(0, 9)
        result += str(n)
        N10 += multipliers[i] * n
    return result + str(N10 % 11 % 10)


def _generate_inn_for_self_employed_physical_person(start_inn):
    multipliers1 = [7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
    multipliers2 = [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
    n11 = 0
    n12 = 0
    result = ""
    for i in range(0, 10):
        n = int(start_inn[i]) if len(start_inn) > i else random.randint(0, 9)
        result += str(n)
        n11 += multipliers1[i] * n
        n12 += multipliers2[i] * n
    n12 += multipliers2[10] * n11
    return result + str(n11 % 11 % 10) + str(n12 % 11 % 10)


def _generate_ogrn_juridical_person(start_ogrn):
    result = ""
    for i in range(0, 12):
        n = int(start_ogrn[i]) if len(start_ogrn) > i else random.randint(0, 9)
        result += str(n)
    return result + str(int(result) % 11)[-1]


def _generate_ogrn_juridical_employed_physical_person(start_ogrn):
    result = ""
    for i in range(0, 14):
        n = int(start_ogrn[i]) if len(start_ogrn) > i else random.randint(0, 9)
        result += str(n)
    return result + str(int(result) % 13)[-1]


def generate(params):
    random.seed()
    if params.type == "ИНН_ЮЛ":
        return _generate_inn_for_juridical_person(params.inn)
    elif params.type == "ИНН_ИП":
        return _generate_inn_for_self_employed_physical_person(params.inn)
    elif params.type == "ОГРН_ЮЛ":
        return _generate_ogrn_juridical_person(params.inn)
    elif params.type == "ОГРН_ИП":
        return _generate_ogrn_juridical_employed_physical_person(params.inn)
    elif params.type == "UUID":
        return str(uuid.uuid4()).upper()
    elif params.type == "UUID":
        return str(uuid.uuid4())

