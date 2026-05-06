import pytest
from clients.courier_client import CourierClient
from data_classes.courier import Courier
from clients.order_client import OrderClient
from data_classes.order import Order

@pytest.fixture(scope="session")
def init_courier_client():
    courier_client = CourierClient()
    return courier_client

@pytest.fixture(scope="session")
def create_courier(init_courier_client):

    courier = Courier()
    print(f"Тестовые данные из фикстуры для создания курьера: {courier.to_dict_correct()}")
    response = init_courier_client.create_courier(courier.to_dict_correct())
    return courier

@pytest.fixture(scope="session")
def init_order_client():
    order_client = OrderClient()
    return order_client

@pytest.fixture(scope="session")
def create_order_obj(init_order_client):

    order = Order()
    print(f"Тестовые данные из фикстуры для создания заказа: {order.to_dict_correct()}")
    response = init_order_client.create(order.to_dict_correct())
    return order
