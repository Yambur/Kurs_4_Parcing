from config import URL_HH
from src.abstract_class_api import WorkWithAbstract
import requests

from src.data_json.work_with_json import WorkWithJson


class RequestHH(WorkWithAbstract):
    """Инициализируем класс, вводим url, определяем ключевое слово и задаем место поиска
    в данном случае он 113, то есть по всей РФ"""
    def __init__(self, keyword, area=113):
        self.url = URL_HH
        self.keyword = keyword
        self.area = area
        self.parameter = {'text': self.keyword, 'area': self.area}

    def request(self):
        """Заносим парсинг в json файл"""
        responce = requests.get(self.url, self.parameter)
        WorkWithJson.save_json(responce.json()['items'])
