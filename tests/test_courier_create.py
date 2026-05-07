import allure
from data_classes.courier import Courier
from data import CourierCreateData

class TestScooterCreateCourier: 

    @allure.description("Создание курьера /api/v1/courier")
    @allure.title("Создание курьера c корректными параметрами")
    def test_create_courier_with_correct_parameters(self, init_courier_client, delete_courier_list):

        courier = Courier()
        data_dictionary = courier.to_dict_correct()
        print(f"Тестовые данные: {data_dictionary}")
        response = init_courier_client.create_courier(data_dictionary)
        body = response.json()
        assert response.status_code == 201
        assert body["ok"] == True
        delete_courier_list.append(courier)

    @allure.description("Создание курьера /api/v1/courier")
    @allure.title("Создание курьера с пустым именем")
    def test_create_courier_with_empty_firstname(self, init_courier_client, delete_courier_list):

        courier = Courier()
        data_dictionary = courier.to_dict_correct(field_to_make_empty = ['firstName'])
        print(f"Тестовые данные: {data_dictionary}")
        response = init_courier_client.create_courier(data_dictionary)
        body = response.json()
        assert response.status_code == 201
        assert body["ok"] == True
        delete_courier_list.append(courier)

    @allure.description("Создание курьера /api/v1/courier")
    @allure.title("Создание курьера с пустым логином")
    def test_create_courier_with_empty_login(self, init_courier_client):

        courier = Courier()
        data_dictionary = courier.to_dict_correct(field_to_make_empty = ['login'])
        print(f"Тестовые данные: {data_dictionary}")
        response = init_courier_client.create_courier(data_dictionary)
        body = response.json()
        assert response.status_code == 400
        assert body["message"] == CourierCreateData.NOT_ENOUGH_DATA

    @allure.description("Создание курьера /api/v1/courier")
    @allure.title("Создание курьера c пустым паролем")
    def test_create_courier_with_empty_password(self, init_courier_client):

        courier = Courier()
        data_dictionary = courier.to_dict_correct(field_to_make_empty = ['password'])
        print(f"Тестовые данные: {data_dictionary}")
        response = init_courier_client.create_courier(data_dictionary)
        body = response.json()
        assert response.status_code == 400
        assert body["message"] == CourierCreateData.NOT_ENOUGH_DATA

    @allure.description("Создание курьера /api/v1/courier")
    @allure.title("Создание курьера c параметрами, по которым уже создан курьер")
    def test_create_courier_when_courier_exist(self, init_courier_client, delete_courier_list):

        courier = Courier()
        data_dictionary = courier.to_dict_correct()
        print(f"Тестовые данные: {data_dictionary}")
        response = init_courier_client.create_courier(data_dictionary)
        print(f"Тестовые данные: {data_dictionary}")
        response = init_courier_client.create_courier(data_dictionary)
        body = response.json()
        assert response.status_code == 409
        assert body["message"] == CourierCreateData.LOGIN_ALREADY_EXIST
        delete_courier_list.append(courier)

    @allure.description("Создание курьера /api/v1/courier")
    @allure.title("Создание курьера c логином, с которым уже создан курьер")
    def test_create_courier_with_existing_login(self, init_courier_client, delete_courier_list):

        courier = Courier()
        data_dictionary = courier.to_dict_correct()
        print(f"Тестовые данные: {data_dictionary}")
        response = init_courier_client.create_courier(data_dictionary)
        login = courier.login
        new_courier_with_existing_login = Courier(login)
        data_dictionary_new_courier = new_courier_with_existing_login.to_dict_correct()
        print(f"Тестовые данные: {data_dictionary_new_courier}")
        response = init_courier_client.create_courier(data_dictionary_new_courier)
        body = response.json()
        assert response.status_code == 409
        assert body["message"] == CourierCreateData.LOGIN_ALREADY_EXIST
        delete_courier_list.append(courier)

    @allure.description("Создание курьера /api/v1/courier")
    @allure.title("Создание курьера без поля имени")
    def test_create_courier_without_field_firstname(self, init_courier_client, delete_courier_list):

        courier = Courier()
        data_dictionary = courier.to_dict_correct(fields_to_remove = ['firstName'])
        print(f"Тестовые данные: {data_dictionary}")
        response = init_courier_client.create_courier(data_dictionary)
        body = response.json()
        assert response.status_code == 201
        assert body["ok"] == True
        delete_courier_list.append(courier)

    @allure.description("Создание курьера /api/v1/courier")
    @allure.title("Создание курьера без поля логина")
    def test_create_courier_without_field_login(self, init_courier_client):

        courier = Courier()
        data_dictionary = courier.to_dict_correct(fields_to_remove = ['login'])
        print(f"Тестовые данные: {data_dictionary}")
        response = init_courier_client.create_courier(data_dictionary)
        body = response.json()
        assert response.status_code == 400
        assert body["message"] == CourierCreateData.NOT_ENOUGH_DATA

    @allure.description("Создание курьера /api/v1/courier")
    @allure.title("Создание курьера без поля пароля")
    def test_create_courier_without_field_password(self, init_courier_client):

        courier = Courier()
        data_dictionary = courier.to_dict_correct(fields_to_remove = ['password'])
        print(f"Тестовые данные: {data_dictionary}")
        response = init_courier_client.create_courier(data_dictionary)
        body = response.json()
        assert response.status_code == 400
        assert body["message"] == CourierCreateData.NOT_ENOUGH_DATA
