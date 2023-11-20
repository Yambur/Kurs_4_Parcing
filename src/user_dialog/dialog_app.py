from src.request.hh import RequestHH
from src.request.sj import RequestSJ
from src.vacancy.vacancy_hh import print_json_hh
from src.vacancy.vacancy_sj import print_json_sj


class Dialog:
    pass

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
            print(print_json_hh())
        elif website == '2':
            keyword = input("Введите ключевое слово по которому будем парсить\n")
            site = RequestSJ(keyword).request()
            print(print_json_sj())
        else:
            print("Такого сайта у нас нет, попробуй еще раз")
            continue

        if site:
            try:
                site.request()
            except Exception as e:
                print(f"Произошла ошибка при запросе данных: {e}")
        break




