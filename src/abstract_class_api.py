from abc import ABC, abstractmethod


class WorkWithAbstract(ABC):
    """Наследуемся от абстрактного класса"""
    @abstractmethod
    def request(self):
        pass