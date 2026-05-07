import allure

class TestScooterGetOrderList: 

    @allure.description("Получение списка заказов /api/v1/orders")
    @allure.title("Получение списка c корректными параметрами")
    def test_get_order_list_with_correct_parameters(self, init_courier_client, create_courier, init_order_client, create_order_obj):

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
        #отправляем запрос на принятие заказа, чтобы затем получить список заказов
        init_order_client.accept_order(courier_id, order_id)
        response = init_order_client.get_order_list(courier_id)
        body = response.json()
        assert response.status_code == 200
        assert len(body["orders"]) >= 1
