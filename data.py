class AcceptOrderData:
                
    NOT_ENOUGH_DATA = "Недостаточно данных для поиска"
    NOT_FOUND = "Not Found."
    NOT_EXISTING_COURIER = "Курьера с таким id не существует"
    NOT_EXISTING_ORDER = "Заказа с таким id не существует"

class CourierCreateData:
                
    NOT_ENOUGH_DATA = 'Недостаточно данных для создания учетной записи'
    LOGIN_ALREADY_EXIST = 'Этот логин уже используется. Попробуйте другой.'

class CourierDeleteData:
                
    NOT_FOUND = "Not Found."
    NOT_EXISTING_COURIER = "Курьера с таким id нет."

class CourierLoginData:
                
    NOT_ENOUGH_DATA = 'Недостаточно данных для входа'
    NOT_EXISTING_COURIER = "Учетная запись не найдена"

class GetOrderNumbersData:
                
    NOT_ENOUGH_DATA = 'Недостаточно данных для поиска'
    NOT_EXISTING_ORDER = "Заказ не найден"
