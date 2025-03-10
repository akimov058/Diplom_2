import allure
import requests
import pytest
from methods.create_user import CreateUser
from data.create_user_data import CreateUserData

class TestCreateUser:
    @allure.title('Создание уникального пользователя')
    def test_create_user(self,generate_random_email,generate_random_password,generate_random_name):
        email = generate_random_email
        password = generate_random_password
        name = generate_random_name
        response = CreateUser.post_create_login(email,password,name)
        with allure.step('Проверяем код и текст ответа'):
            assert response.status_code == 200 and 'true' in response.text

    @allure.title('Создание пользователя, который уже зарегистрирован')
    def test_create_user_create_exist_user_error(self,generate_random_email,generate_random_password,generate_random_name):
        email = generate_random_email
        password = generate_random_password
        name = generate_random_name
        response = CreateUser.post_create_login(email,password,name)
        response_error = CreateUser.post_create_login(email,password,name)
        with allure.step('Проверяем код и текст ответа'):
            assert response_error.status_code == 403 and response_error.json()['message'] ==CreateUserData.TEXT_CREATE_USER_403



