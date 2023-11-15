from config import URL_SJ
from src.abstract_class_api import WorkWithAbstract
import requests

from src.data_json.work_with_json import WorkWithJson


class RequestsSJ(WorkWithAbstract):
    def __init__(self, keyword, page=1):
        self.url = URL_SJ
        self.params = {'keywords': keyword, 'page': page}

    def request(self):
        headers = {
            'X-Api-App-Id': 'v3.r.137951623.25fdf6a929d7a2b8a7c0f7c14fc329fd96912622.c8c509bdc2d0cc6f3023e1f179ea68bdcc9c05ff'}
        responce = requests.get(self.url, params=self.params, headers=headers)
        return WorkWithJson.save_json(responce.json()['objects'])
