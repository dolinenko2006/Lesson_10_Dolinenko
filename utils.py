# `load_candidates()`, которая загрузит данные из файла

# `get_all()`, которая покажет всех кандидатов
#
# `get_by_pk(pk)`, которая вернет кандидата по pk

# `get_by_skill(skill_name)`, которая вернет кандидатов по навыку

import json

def load_candidates():
    """
    загрузит данные из файла
    :return: список result_json из candidates.json
    """
    with open("candidates.json", "r", encoding='utf-8') as file:
        result_json = json.load(file)
        return result_json

# def get_all():
#     """
#     покажет всех кандидатов
#     :return: список кандидатов
#     """
#     return load_candidates()

def get_by_pk(pk):
    """
    вернет кандидата по pk
    :param pk: порядковый номер
    :return: имя кандидата
    """
    for candidate in load_candidates():
        if pk == candidate["pk"]:
            return candidate
    return

def get_by_skill(skill):
    """
    вернет кандидатов по навыку
    :param skill: навык "go, python"
    :return: список кандидатов (именна)
    """
    candidates_with_skill = []
    for candidate in load_candidates():
        if skill.lower() in candidate["skills"].lower().split(", "):
            candidates_with_skill.append(candidate)
    return candidates_with_skill
