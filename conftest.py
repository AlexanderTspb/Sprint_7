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
def create_courier(init_courier_client, delete_courier_list):

    courier = Courier()
    data_dictionary_courier = courier.to_dict_correct()
    print(f"Тестовые данные из фикстуры для создания курьера: {data_dictionary_courier}")
    response = init_courier_client.create_courier(data_dictionary_courier)
    yield courier
    print("ДОШЛИ ЛИ ДО КОДА ПОСЛЕ YIELD")
    if response.status_code == 201:
        print("Вызвали из фикстуры create_courier")
        delete_courier_list.append(courier)

@pytest.fixture(scope="session")
def delete_courier_list(init_courier_client):
    
    # Контейнер для данных, требующих очистки
    couriers_to_delete = []
    yield couriers_to_delete
    # Teardown: удаляем все накопленные элементы
    if len(couriers_to_delete) > 0:
        for courier in couriers_to_delete:
            print(f"Вошли в фикстуру delete_courier_list")
            data_dictionary_login = courier.to_dict_correct(fields_to_remove = ['firstName'])
            print(f"тестовые данные в фикстуре delete_courier_list {data_dictionary_login}")
            response_login = init_courier_client.login_courier(data_dictionary_login)
            if(response_login.status_code) == 200:
                print(f"Удаляем через фикстуру delete_courier_list")
                body_response_login  = response_login.json()
                courier_id = body_response_login["id"]
                response_delete = init_courier_client.delete_courier(courier_id)

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
