import requests
import allure

class BaseClient:
    BASE_URL = "https://qa-scooter.praktikum-services.ru/"

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    @allure.step('Отправляем запрос {method} https://qa-scooter.praktikum-services.ru/{path}')
    def request(self, method, path, **kwargs):
        url = self.BASE_URL + path
        response = self.session.request(method, url, **kwargs)
        return response
    