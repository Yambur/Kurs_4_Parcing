import json


class VacancyHH:
    def __init__(self, title, city, requirements,description, salary_from, salary_to):
        self.title = title
        self.city = city
        self.requirements = requirements
        self.description = description
        self.salary_from = salary_from
        self.salary_to = salary_to

    def __repr__(self):
        return (f'Вакансия: {self.title} \n'
                f'Город: {self.city} \n'
                f'Знания: {self.requirements} \n'
                f'Описание: {self.description} \n'
                f'Зарплата от: {self.salary_from} \n'
                f'Зарплата до: {self.salary_to} \n'
                '')


with open('../../cache_json/cache_hh.json', 'r', encoding='utf-8') as file:
    vacancy = json.load(file)
    vacancy_s = []
    for i in vacancy:
        if 'name' in i and 'area' in i and 'snippet' in i and i['salary'] is not None and 'from' in i['salary']:
            vacancy_s.append(VacancyHH(i['name'], i['area']['name'], i['snippet']['requirement'], i['snippet']['responsibility'], i['salary']['from'],
                                     i['salary']['to']))
        else:
            pass
for vacancy in vacancy_s:
    print(vacancy)
