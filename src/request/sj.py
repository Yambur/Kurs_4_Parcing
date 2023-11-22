from api_key_sj import api_key
from config import URL_SJ
from src.abstract_class_api import WorkWithAbstract
import requests

from src.data_json.work_with_json import WorkWithJson

class RequestSJ(WorkWithAbstract):
    """Инициализируем класс, вводим url, определяем ключевое слово и страницу поиска"""
    def __init__(self, keyword, page=1):
        self.url = URL_SJ
        self.keyword = keyword
        self.params = {'keywords': keyword, 'page': page}

    def request(self):
        """Заносим парсинг в json файл"""
        headers = {'X-Api-App-Id': api_key}
        responce = requests.get(self.url, params=self.params, headers=headers)
        return WorkWithJson.save_json(responce.json()['objects'])
