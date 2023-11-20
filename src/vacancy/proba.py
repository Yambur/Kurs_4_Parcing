from src.request.hh import RequestHH
from src.request.sj import RequestSJ

from src.vacancy.vacancy_hh import vacancy_s
from src.vacancy.vacancy_sj import vacancy_sj

print("Привет, давай спарсим сайт")
print("Давай ты выберешь цифру сайта и нажмешь ENTER")
print("1 - HeadHunter")
print("2 - SuperJob")
while True:
    website = input()
    site = None  # Значение по умолчанию
    if website == '1':
        keyword = input("Введите ключевое слово по которому будем парсить\n")
        site = RequestHH(keyword)

    elif website == '2':
        keyword = input("Введите ключевое слово по которому будем парсить\n")
        site = RequestSJ(keyword)
        #for vacancy_object in vacancy_sj:
        #    print(vacancy_object)
    else:
        print("Такого сайта у нас нет, попробуй еще раз")
        continue

    if site:
        try:
            site.request()
        except Exception as e:
            print(f"Произошла ошибка при запросе данных: {e}")

    break

# рабочая схема для выдергивания вакансий из уже сделаного джейсона
"""if website == '1':
    for vacancy_obj in vacancy_s:
        print(vacancy_obj)
elif website == '2':
    for vacancy_object in vacancy_sj:
        print(vacancy_object)
else:
    print("Такого сайта у нас нет, выберите еще раз")"""
