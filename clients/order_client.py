from clients.base_client import BaseClient
import allure

class OrderClient(BaseClient):

    ORDER_PATH = "api/v1/orders"

    @allure.step('Отправляем запрос на создание заказа {order}')
    def create(self, order):
        response = self.request(
            "POST",
            self.ORDER_PATH,
            json=order
        )
        return response
    
    @allure.step('Отправляем запрос на получение номера заказа по номеру трека {order_track}')
    def get_order_number(self, order_track):
        response = self.request(
            "GET",
            f"{self.ORDER_PATH}/track",
            params={"t": order_track}
        )
        return response
    
    @allure.step('Отправляем запрос на принятие заказа по id курьера {courier_id} и id заказа {order_id}')
    def accept_order(self, courier_id, order_id):
        
        response = self.request(
            "PUT",
            f"{self.ORDER_PATH}/accept/{order_id}",
            params={"courierId": courier_id}
        )
        return response
    
    @allure.step('Отправляем запрос на получение списка заказов по id курьера {courier_id}')
    def get_order_list(self, courier_id):
        response = self.request(
            "GET",
            self.ORDER_PATH,
            params={"courierId": courier_id}
        )
        return response

    @allure.step('Отправляем запрос на получение списка заказов без id курьера')
    def get_order_number_without_track(self):
        response = self.request(
            "GET",
            f"{self.ORDER_PATH}/track"
        )
        return response

    @allure.step('Отправляем запрос на принятие заказа без id курьера, но с id заказа {order_id}')
    def accept_order_without_courier(self, order_id):

        response = self.request(
            "PUT",
            f"{self.ORDER_PATH}/accept/{order_id}"
        )
        return response
    
    @allure.step('Отправляем запрос на принятие заказа по id курьера {courier_id} и без id заказа')
    def accept_order_without_order_id(self, courier_id):
        
        response = self.request(
            "PUT",
             f"{self.ORDER_PATH}/accept/",
             params={"courierId": courier_id}
        )
        return response
    