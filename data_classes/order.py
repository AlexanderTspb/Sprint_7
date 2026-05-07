from faker import Faker
import random

fake = Faker('ru_RU')

class Order:

    def __init__(self, first_name=None, last_name=None, address=None, metro_station=None, phone=None, rent_time=None, delivery_date=None, comment=None, color=None):
        self.first_name = first_name if first_name is not None else fake.first_name()
        self.last_name = last_name if last_name is not None else fake.last_name()
        self.address = address if address is not None else fake.address()
        self.metro_station = metro_station if metro_station is not None else random.randint(1, 25)
        self.phone = phone if phone is not None else fake.phone_number()
        self.rent_time = rent_time if rent_time is not None else random.randint(1, 25)
        self.delivery_date = delivery_date if delivery_date is not None else fake.date_between(start_date='today', end_date='+8w').strftime('%Y-%m-%d')
        self.comment = comment if comment is not None else fake.text(max_nb_chars=25)
        self.color = color if color is not None else random.choice([["GREY"], ["BLACK"]])
        self.order_dictionary = {  
            "firstName": self.first_name,
            "lastName": self.last_name,
            "address": self.address,
            "metroStation": self.metro_station,
            "phone": self.phone,
            "rentTime": self.rent_time,
            "deliveryDate": self.delivery_date,
            "comment": self.comment,
            "color": self.color
        }

    def to_dict_correct(self, fields_to_remove=None, field_to_make_empty = None, updated_dictionary = None):
        
        temp_dict = self.order_dictionary.copy()
        if updated_dictionary is not None:
            self.update_dictionary(temp_dict, updated_dictionary)
        if field_to_make_empty:
            self.make_empty_dictionary_fields(temp_dict, field_to_make_empty)
        if fields_to_remove:
            self.remove_dictionary_fields(temp_dict, fields_to_remove)
        return temp_dict
    
    def update_dictionary(self, original_dictionary, update_dictionary):
        for key, value in update_dictionary.items():
            if key in original_dictionary:
                original_dictionary[key] = value
        return original_dictionary
    
    def remove_dictionary_fields(self, original_dictionary, fields_to_remove):
        for field in fields_to_remove:
            original_dictionary.pop(field, None)
        return original_dictionary
    
    def make_empty_dictionary_fields(self, original_dictionary, field_to_make_empty):
        for field in field_to_make_empty:
            if field in original_dictionary:
                original_dictionary[field] = ""
        return original_dictionary
    