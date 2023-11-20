import pytest

class VacancySJ:
    pass

def test_vacancy_repr():
    vacancy = VacancySJ("Software Engineer", "New York", "Python developer", 60000, 90000)
    expected_repr = ("\nВакансия: Software Engineer \n"
                     "Город: New York \n"
                     "Описание и требования: Python developer \n"
                     "Зарплата от 60000 до 90000\n"
                     "--------------------------------------------------\n")
    assert repr(vacancy) == expected_repr