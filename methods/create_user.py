import requests
import allure

class CreateUser:
    @staticmethod
    @allure.step('Вызываем метод создания пользователя')
    def post_create_login(email,password,name):
        payload = {
    "email": email,
    "password": password,
    "name":name
}
        response = requests.post()
        return response