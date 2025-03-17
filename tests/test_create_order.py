import allure
from methods.base_api import BaseApi
from methods.create_order_api import CreateOrderApi

class TestCreateOrder:
    @allure.title('Создание заказа с авторизацией')
    def test_create_order_with_authorization(self,generate_random_email,generate_random_password,generate_random_name):
        email = generate_random_email
        password = generate_random_password
        name = generate_random_name
        response_create_user = BaseApi.post_create_login(email,password,name)
        token = response_create_user.json()['accessToken']
        response_create_order = CreateOrderApi.post_create_order(token)
        assert response_create_order.status_code == 200 and response_create_order.json()['success']==True

    @allure.title('Создание заказа без авторизации')
    def test_create_order_not_authorization(self):
        response_create_order = CreateOrderApi.post_create_order('')
        assert response_create_order.status_code == 200 and response_create_order.json()['success']==True

