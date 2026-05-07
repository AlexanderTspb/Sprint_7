import pytest
import allure

from data_classes.order import Order

class TestScooterCreateOrder: 

    @allure.description("Создание заказа /api/v1/orders")
    @allure.title("Создание заказа c корректными параметрами")
    @pytest.mark.parametrize(
        'colors',            
        [
            ['BLACK'],
            ['BLACK', 'GREY'],
            []
        ]
    )
    def test_create_order_with_correct_parameters(self, init_order_client, colors):

        order = Order(color=colors)
        data_dictionary = order.to_dict_correct()
        print(f"Тестовые данные: {data_dictionary}")
        response = init_order_client.create(data_dictionary)
        body = response.json()
        assert response.status_code == 201
        assert body["track"] is not None
