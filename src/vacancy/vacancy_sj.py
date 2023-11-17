import json


class VacancySJ:
    def __init__(self, title, city, description, salary_from, salary_to):
        self.title = title
        self.city = city
        self.description = description
        self.salary_from = salary_from
        self.salary_to = salary_to

    def __repr__(self):
        return (f'Вакансия: {self.title} \n'
                f'Город: {self.city} \n'
                f'Описание и требования: {self.description} \n'
                f'Зарплата от: {self.salary_from} \n'
                f'Зарплата до: {self.salary_to} \n'
                '')


with open('../../cache_json/cache_hh.json', 'r', encoding='utf-8') as file:
    vacancy = json.load(file)
    vacancy_s = []
    for i in vacancy:
        vacancy_s.append(
            VacancySJ(i['profession'], i['town']['title'], i['candidat'], i['payment_from'], i['payment_to']))
for vacancy in vacancy_s:
    print(vacancy)
