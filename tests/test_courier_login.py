import allure
from data import CourierLoginData

class TestScooterLoginCourier: 

    @allure.description("Логин курьера /api/v1/courier/login")
    @allure.title("Логин курьера c корректными параметрами")
    def test_login_courier_with_correct_parameters(self, init_courier_client, create_courier):

        data_dictionary = create_courier.to_dict_correct(fields_to_remove = ['firstName'])
        response = init_courier_client.login_courier(data_dictionary)
        body = response.json()
        assert response.status_code == 200
        assert body["id"] is not None

    @allure.description("Логин курьера /api/v1/courier/login")
    @allure.title("Логин курьера без поля логина")
    def test_login_courier_without_login_field(self, init_courier_client, create_courier):

        data_dictionary = create_courier.to_dict_correct(fields_to_remove = ['firstName', 'login'])
        response = init_courier_client.login_courier(data_dictionary)
        body = response.json()
        assert response.status_code == 400
        assert body["message"] == CourierLoginData.NOT_ENOUGH_DATA

    @allure.description("Логин курьера /api/v1/courier/login")
    @allure.title("Логин курьера с пустым логином")
    def test_login_courier_with_empty_login(self, init_courier_client, create_courier):

        data_dictionary = create_courier.to_dict_correct(fields_to_remove = ['firstName'], field_to_make_empty = ['login'])
        response = init_courier_client.login_courier(data_dictionary)
        body = response.json()
        assert response.status_code == 400
        assert body["message"] == CourierLoginData.NOT_ENOUGH_DATA

    @allure.description("Логин курьера /api/v1/courier/login")
    @allure.title("Логин курьера с пустым паролем")
    def test_login_courier_with_empty_password(self, init_courier_client, create_courier):

        data_dictionary = create_courier.to_dict_correct(fields_to_remove = ['firstName'], field_to_make_empty = ['password'])
        response = init_courier_client.login_courier(data_dictionary)
        body = response.json()
        assert response.status_code == 400
        assert body["message"] == CourierLoginData.NOT_ENOUGH_DATA

    @allure.description("Логин курьера /api/v1/courier/login")
    @allure.title("Логин курьера с некорректным логином")
    def test_login_courier_with_incorrect_login(self, init_courier_client, create_courier):

        updated_dictionary = {'login': f'{create_courier.login}i'}
        data_dictionary = create_courier.to_dict_correct(fields_to_remove = ['firstName'], updated_dictionary = updated_dictionary)
        response = init_courier_client.login_courier(data_dictionary)
        body = response.json()
        assert response.status_code == 404
        assert body["message"] == CourierLoginData.NOT_EXISTING_COURIER
    
    @allure.description("Логин курьера /api/v1/courier/login")
    @allure.title("Логин курьера с некорректным паролем")
    def test_login_courier_with_incorrect_password(self, init_courier_client, create_courier):

        updated_dictionary = {'password': f'{create_courier.password}i'}
        data_dictionary = create_courier.to_dict_correct(fields_to_remove = ['firstName'], updated_dictionary = updated_dictionary)
        response = init_courier_client.login_courier(data_dictionary)
        body = response.json()
        assert response.status_code == 404
        assert body["message"] == CourierLoginData.NOT_EXISTING_COURIER

    @allure.description("Логин курьера /api/v1/courier/login")
    @allure.title("Логин курьера без поля пароля")
    def test_login_courier_without_password_field(self, init_courier_client, create_courier):

        data_dictionary = create_courier.to_dict_correct(fields_to_remove = ['firstName','password'])
        response = init_courier_client.login_courier(data_dictionary)
        assert response.status_code == 504
