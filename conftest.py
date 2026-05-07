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
    response = init_courier_client.create_courier(data_dictionary_courier)
    yield courier
    if response.status_code == 201:
        delete_courier_list.append(courier)

@pytest.fixture(scope="session")
def delete_courier_list(init_courier_client):
    
    couriers_to_delete = []
    yield couriers_to_delete
    if len(couriers_to_delete) > 0:
        for courier in couriers_to_delete:
            data_dictionary_login = courier.to_dict_correct(fields_to_remove = ['firstName'])
            response_login = init_courier_client.login_courier(data_dictionary_login)
            if(response_login.status_code) == 200:
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
    response = init_order_client.create(order.to_dict_correct())
    return order
