from src.request.hh import RequestHH
from src.request.sj import RequestSJ
from src.vacancy.vacancy_hh import print_json_hh
from src.vacancy.vacancy_sj import print_json_sj


class Dialog:
    pass
    """Начинаем диалог с пользователем и выбираем сайт для парсинга.
    Затем вводим ключевое слово"""
    print("Привет, давай спарсим сайт")
    print("Давай ты выберешь цифру сайта и нажмешь ENTER")
    print("1 - HeadHunter")
    print("2 - SuperJob")
    while True:
        website = input()
        site = None  # Значение по умолчанию
        if website == '1':
            keyword = input("Введите ключевое слово по которому будем парсить\n")
            site = RequestHH(keyword).request()
            sort_hh = print_json_hh()
            sort_hh.sort(key=lambda x: x.salary_to, reverse=True)
            print("Обратите внимание, что вакансии показываются от большей з/п к меньшей")
            print("Укажите сколько вакансий вы хотели бы посмотреть цифрой\n"
                  "Если хотите посмотреть весь список, то напишите слово 'все'")
            user_vacancy = input()
            if user_vacancy.lower() == 'все':
                print(sort_hh)
            else:
                try:
                    num_vacancies = int(user_vacancy)
                    print(sort_hh[:num_vacancies])
                except ValueError:
                    print("Пожалуйста, введите число или 'все'")
        elif website == '2':
            keyword = input("Введите ключевое слово по которому будем парсить\n")
            site = RequestSJ(keyword).request()
            sort_sj = print_json_sj()
            print("Обратите внимание, что вакансии показываются от большей з/п к меньшей")
            print("Укажите сколько вакансий вы хотели бы посмотреть\n"
                  "Если хотите посмотреть весь список, то напишите слово 'все'")
            user_vacancy = input()
            if user_vacancy.lower() == 'все':
                print(sort_sj)
            else:
                try:
                    num_vacancies = int(user_vacancy)
                    print(sort_sj[:num_vacancies])
                except ValueError:
                    print("Пожалуйста, введите число или 'все'")
        else:
            """Зацикливаем метод, пока пользователю не надоест баловаться
            и он не введет нужную нам цифру"""
            print("Такого сайта у нас нет, попробуй еще раз")
            continue

        if site:
            try:
                site.request()
            except Exception as e:
                print(f"Произошла ошибка при запросе данных: {e}")
        break




