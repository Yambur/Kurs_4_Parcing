# Курсовая № 4. Парсинг сайтов HH и SJ

## Что позволяет делать программа:

- Выбирать сайт для парсинга
- Выбирать ключевое слово для поиска
- Сортировать вакансии по зарплате

## Основные классы для работы:

`RequestHH`- вытаскивает с сайта HH информацию и записывает их в json

`RequestSJ`- вытаскивает с сайта SJ информацию и записывает их в json

`VacancyHH` и `VacancySJ` - выцепляет из json файла интересующие нас параметры и выдает на экран

## Класс Dialog:
>Используется для взаимодействия с пользователем
- Узнает интересующий сайт
- Узнает ключевое слово
- Выдает информацию на экран
