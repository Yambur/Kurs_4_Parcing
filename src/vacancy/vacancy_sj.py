import json

from config import JSON_JS


class VacancySJ:
    def __init__(self, title, city, description, salary_from, salary_to):
        self.title = title
        self.city = city
        self.description = description
        self.salary_from = salary_from
        self.salary_to = salary_to

    def __repr__(self):
        return (f'\nВакансия: {self.title} \n'
                f'Город: {self.city} \n'
                f'Описание и требования: {self.description} \n'
                f'Зарплата от {self.salary_from} до {self.salary_to}\n'
                f"{'-' * 50}\n")


def print_json_sj():
    with open(JSON_JS, 'r', encoding='utf-8') as file:
        vacancy = json.load(file)
        vacancy_sj = []
        for i in vacancy:
            vacancy_sj.append(
                VacancySJ(i['profession'], i['town']['title'], i['candidat'], i['payment_from'], i['payment_to']))
    return vacancy_sj
