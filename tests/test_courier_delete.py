import allure
from data import CourierDeleteData

class TestScooterDeleteCourier: 

    @allure.description("Удаление курьера /api/v1/courier/:id")
    @allure.title("Удаление курьера c корректными параметрами")
    def test_delete_courier_with_correct_parameters(self, init_courier_client, create_courier):

        data_dictionary_courier = create_courier.to_dict_correct(fields_to_remove = ['firstName'])
        print(f"Тестовые данные: {data_dictionary_courier}")
        #отправляем запрос на логин, чтобы затем получить id курьера
        response = init_courier_client.login_courier(data_dictionary_courier)
        body = response.json()
        #получаем id курьера
        courier_id =  body["id"]
        response_delete = init_courier_client.delete_courier(courier_id)
        body = response_delete.json()
        assert response_delete.status_code == 200
        assert body["ok"] == True

    @allure.description("Удаление курьера /api/v1/courier/:id")
    @allure.title("Удаление курьера без id курьера")
    def test_delete_courier_without_courier_id(self, init_courier_client):

        response_delete = init_courier_client.delete_courier_without_id()
        body = response_delete.json()
        assert response_delete.status_code == 404
        assert body["message"] == CourierDeleteData.NOT_FOUND

    @allure.description("Удаление курьера /api/v1/courier/:id")
    @allure.title("Удаление курьера c несуществующим id курьера")
    def test_delete_courier_with_incorrect_courier_id(self, init_courier_client):

        courier_id =  "000000"
        response_delete = init_courier_client.delete_courier(courier_id)
        body = response_delete.json()
        assert response_delete.status_code == 404
        assert body["message"] == CourierDeleteData.NOT_EXISTING_COURIER
