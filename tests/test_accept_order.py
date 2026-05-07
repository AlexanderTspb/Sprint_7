import allure
from data import AcceptOrderData

class TestScooterAcceptOrder: 

    @allure.description("Принятие заказа /api/v1/orders/accept/:id")
    @allure.title("Принятие заказа c корректными параметрами")
    def test_accept_order_with_correct_parameters(self, init_courier_client, create_courier, init_order_client, create_order_obj):

        print("*****Тест*****")
        
        data_dictionary_courier = create_courier.to_dict_correct(fields_to_remove = ['firstName'])
        print(f"Тестовые данные: {data_dictionary_courier}")
        #отправляем запрос на логин, чтобы затем получить id курьера
        response = init_courier_client.login_courier(data_dictionary_courier)
        body = response.json()
        #получаем id курьера
        courier_id =  body["id"]
        #создаем заказ
        data_dictionary_order = create_order_obj.to_dict_correct()
        #отправляем запрос на создание заказа, чтобы затем получить номер трека
        response_order = init_order_client.create(data_dictionary_order)
        body = response_order.json()
        #получаем номер трека
        order_track =  body["track"]
        #отправляем запрос на получение номера заказа, чтобы затем получить id заказа
        response_order_number = init_order_client.get_order_number(order_track)
        body = response_order_number.json()
        #по номеру трека получаем id заказа
        order_id = body["order"]['id']
        #отправляем запрос на принятие заказа
        response_accept_order = init_order_client.accept_order(courier_id, order_id)
        body = response_accept_order.json()
        assert response_accept_order.status_code == 200
        assert body['ok'] == True
        

    @allure.description("Принятие заказа /api/v1/orders/accept/:id")
    @allure.title("Принятие заказа c пустым id курьера")
    def test_accept_order_with_empty_courier_id(self, init_order_client, create_order_obj):

        print("*****Тест*****")
        
        courier_id = ""
        #создаем заказ
        data_dictionary_order = create_order_obj.to_dict_correct()
        #отправляем запрос на создание заказа, чтобы затем получить номер трека
        response_order = init_order_client.create(data_dictionary_order)
        body = response_order.json()
        #получаем номер трека
        order_track =  body["track"]
        #отправляем запрос на получение номера заказа, чтобы затем получить id заказа
        response_order_number = init_order_client.get_order_number(order_track)
        body = response_order_number.json()
        #по номеру трека получаем id заказа
        order_id = body["order"]['id']
        #отправляем запрос на принятие заказа
        response_accept_order = init_order_client.accept_order(courier_id, order_id)
        body = response_accept_order.json()
        assert response_accept_order.status_code == 400
        assert body['message'] == AcceptOrderData.NOT_ENOUGH_DATA


    @allure.description("Принятие заказа /api/v1/orders/accept/:id")
    @allure.title("Принятие заказа без id курьера")
    def test_accept_order_without_courier_id(self, init_order_client, create_order_obj):

        print("*****Тест*****")
        
        #создаем заказ
        data_dictionary_order = create_order_obj.to_dict_correct()
        #отправляем запрос на создание заказа, чтобы затем получить номер трека
        response_order = init_order_client.create(data_dictionary_order)
        body = response_order.json()
        #получаем номер трека
        order_track =  body["track"]
        #отправляем запрос на получение номера заказа, чтобы затем получить id заказа
        response_order_number = init_order_client.get_order_number(order_track)
        body = response_order_number.json()
        #по номеру трека получаем id заказа
        order_id = body["order"]['id']
        #отправляем запрос на принятие заказа
        response_accept_order = init_order_client.accept_order_without_courier(order_id)
        body = response_accept_order.json()
        assert response_accept_order.status_code == 400
        assert body['message'] == AcceptOrderData.NOT_ENOUGH_DATA
        
    @allure.description("Принятие заказа /api/v1/orders/accept/:id")
    @allure.title("Принятие заказа без id заказа")
    def test_accept_order_without_order_id(self, init_courier_client, create_courier, init_order_client):

        print("*****Тест*****")
        
        data_dictionary_courier = create_courier.to_dict_correct(fields_to_remove = ['firstName'])
        print(f"Тестовые данные: {data_dictionary_courier}")
        #отправляем запрос на логин, чтобы затем получить id курьера
        response = init_courier_client.login_courier(data_dictionary_courier)
        body = response.json()
        #получаем id курьера
        courier_id =  body["id"]
        #отправляем запрос на принятие заказа
        response_accept_order = init_order_client.accept_order_without_order_id(courier_id)
        body = response_accept_order.json()
        assert response_accept_order.status_code == 404
        assert body['message'] == AcceptOrderData.NOT_FOUND

    @allure.description("Принятие заказа /api/v1/orders/accept/:id")
    @allure.title("Принятие заказа c некорректным id курьера")
    def test_accept_order_with_incorrect_courier_id(self, init_order_client, create_order_obj):

        print("*****Тест*****")
        
        courier_id = "000000"
        #создаем заказ
        data_dictionary_order = create_order_obj.to_dict_correct()
        #отправляем запрос на создание заказа, чтобы затем получить номер трека
        response_order = init_order_client.create(data_dictionary_order)
        body = response_order.json()
        #получаем номер трека
        order_track =  body["track"]
        #отправляем запрос на получение номера заказа, чтобы затем получить id заказа
        response_order_number = init_order_client.get_order_number(order_track)
        body = response_order_number.json()
        #по номеру трека получаем id заказа
        order_id = body["order"]['id']
        #отправляем запрос на принятие заказа
        response_accept_order = init_order_client.accept_order(courier_id, order_id)
        body = response_accept_order.json()
        assert response_accept_order.status_code == 404
        assert body['message'] == AcceptOrderData.NOT_EXISTING_COURIER
        
    @allure.description("Принятие заказа /api/v1/orders/accept/:id")
    @allure.title("Принятие заказа c некорректным id заказа")
    def test_accept_order_with_incorrect_order_id(self, init_courier_client, create_courier, init_order_client):

        print("*****Тест*****")
        
        data_dictionary_courier = create_courier.to_dict_correct(fields_to_remove = ['firstName'])
        print(f"Тестовые данные: {data_dictionary_courier}")
        #отправляем запрос на логин, чтобы затем получить id курьера
        response = init_courier_client.login_courier(data_dictionary_courier)
        body = response.json()
        #получаем id курьера
        courier_id =  body["id"]
        order_id = "000000"
        #отправляем запрос на принятие заказа
        response_accept_order = init_order_client.accept_order(courier_id, order_id)
        body = response_accept_order.json()
        assert response_accept_order.status_code == 404
        assert body['message'] == AcceptOrderData.NOT_EXISTING_ORDER
