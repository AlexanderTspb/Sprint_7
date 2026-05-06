from clients.base_client import BaseClient
import allure

class CourierClient(BaseClient):

    COURIER_PATH = "api/v1/courier"

    @allure.step('Отправляем запрос на создание курьера {courier}')
    def create_courier(self, courier):
        response = self.request(
            "POST",
            self.COURIER_PATH,
            json=courier
        )
        self.print_response(response, "запрос на создание курьера")
        return response

    @staticmethod
    def print_response(response, request_name):
        print(f"Ответ на {request_name}: {response.text} \n ------")

    @allure.step('Отправляем запрос на логин курьера {login}')
    def login_courier(self, login):
        response = self.request(
            "POST",
            f"{self.COURIER_PATH}/login",
            json=login
        )
        self.print_response(response, "запрос на логин курьера")
        return response
    
    @allure.step('Отправляем запрос на удаление курьера по id курьера {courier_id}')
    def delete_courier(self, courier_id):
        response = self.request(
            "DELETE",
            f"{self.COURIER_PATH}/{courier_id}"
        )
        self.print_response(response, "запрос на удаление курьера")
        return response

    @allure.step('Отправляем запрос на удаление курьера без id курьера')
    def delete_courier_without_id(self):
        response = self.request(
            "DELETE",
            f"{self.COURIER_PATH}/"
        )
        self.print_response(response, "запрос на удаление курьера без id")
        return response
