import allure

class TestScooterGetOrderNumber: 

    @allure.description("Получение заказа по его номеру /api/v1/orders/track")
    @allure.title("Получение заказа по его номеру c корректными параметрами")
    def test_get_order_number_with_correct_parameters(self, init_order_client, create_order_obj):

        #создаем заказ
        data_dictionary_order = create_order_obj.to_dict_correct()
        #отправляем запрос на создание заказа, чтобы затем получить номер трека
        print(f"Тестовые данные: {data_dictionary_order}")
        response_order = init_order_client.create(data_dictionary_order)
        assert response_order.status_code == 201
        body = response_order.json()
        #получаем номер трека
        order_track =  body["track"]
        response_order_number = init_order_client.get_order_number(order_track)
        body = response_order_number.json()
        assert response_order_number.status_code == 200
        assert body["order"]['id'] is not None

    @allure.description("Получение заказа по его номеру /api/v1/orders/track")
    @allure.title("Получение заказа по его номеру c пустым номером трека")
    def test_get_order_number_with_empty_track(self, init_order_client):

        order_track =  ""
        response_order_number = init_order_client.get_order_number(order_track)
        body = response_order_number.json()
        assert response_order_number.status_code == 400
        assert body["message"] == "Недостаточно данных для поиска"
        
    @allure.description("Получение заказа по его номеру /api/v1/orders/track")
    @allure.title("Получение заказа по его номеру без параметра трека")
    def test_get_order_number_without_track(self, init_order_client):

        response_order_number = init_order_client.get_order_number_without_track()
        body = response_order_number.json()
        assert response_order_number.status_code == 400
        assert body["message"] == "Недостаточно данных для поиска"

    @allure.description("Получение заказа по его номеру /api/v1/orders/track")
    @allure.title("Получение заказа по его номеру c несуществующим треком")
    def test_get_order_number_with_not_existing_track(self, init_order_client):

        order_track =  "000000"
        response_order_number = init_order_client.get_order_number(order_track)
        body = response_order_number.json()
        assert response_order_number.status_code == 404
        assert body["message"] == "Заказ не найден" 
        