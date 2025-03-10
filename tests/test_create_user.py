import allure
import requests
import pytest
from methods.create_user import CreateUser

class TestCreateUser:
    @allure.title('Создание уникального пользователя')
    def test_create_user(self,generate_random_email,generate_random_password,generate_random_name):
        email = generate_random_email
        password = generate_random_password
        name = generate_random_name
        response = CreateUser.post_create_login(email,password,name)
        with allure.step('Проверяем код и текст ответа'):
            assert response.status_code == 200 and 'success' in response.text



