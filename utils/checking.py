""""Методы для проверки ответов"""
import json

from requests import Response

class Cheking():

    """Метод для проверки статус кода"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print("Успешно!!! Статус код = " + str(response.status_code))
        else:
            print("Провал!!! Статус код = " + str(response.status_code))

    """"Методы для проверки наличия полей в ответе запроса"""
    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("Все поля присутствуют")

    """"Методы для проверки значений обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_value(response: Response, field_name, expexted_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expexted_value
        print(field_name + " верен !!!")

    """"Методы для проверки значений обязательных полей в ответе запроса по заданному слову"""
    @staticmethod
    def check_json_search_word_in_value(response: Response, field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print("Слово " + search_word + " присутствует !!!")
        else:
            print("Слово " + search_word + " отсутствует !!!")