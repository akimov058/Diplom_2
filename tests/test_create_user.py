import allure
import requests
import pytest

class TestCreateUser:
    @allure.title('Создание уникального пользователя')
    def test_create_user(self,generate_random_email,generate_random_password,generate_random_name):
        email = generate_random_email
        password = generate_random_password
        name = generate_random_name

