from faker import Faker
import random
import string

fake = Faker('ru_RU')

class Courier:

    def __init__(self, login=None, password=None, first_name=None):
        self.login = login if login is not None else self.create_user_name()
        self.password = password if password is not None else fake.password(length=10)
        self.first_name = first_name if first_name is not None else fake.first_name()
        self.courier_dictionary = {  
            "login": self.login,
            "password": self.password,            
            "firstName": self.first_name
        }

    def create_user_name(self):
        random_letter = random.choice(string.ascii_lowercase)
        user_name = f'{fake.user_name()}{random_letter}{random.randint(1, 999)}'
        return user_name

    def to_dict_correct(self, fields_to_remove=None, field_to_make_empty = None, updated_dictionary = None):
        temp_dict = self.courier_dictionary.copy()
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
    




    def to_dict_with_empty_fields_test(self, empty_login = False, empty_password = False, empty_first_name = False):
        temp_dict = self.courier_dictionary.copy()
        if empty_login:
            temp_dict['login'] = ''
        if empty_password:
            temp_dict['password'] = ''
        if empty_first_name:
            temp_dict['firstName'] = '' 
        return temp_dict
    
    def to_dict_correct_test(self, remove_login = False, remove_password = False, remove_first_name = False):
        if remove_login:
            self.dictionary.pop("login")
        if remove_password:
            self.dictionary.pop("password")
        if remove_first_name:
             self.dictionary.pop("firstName") 
        return self.dictionary
