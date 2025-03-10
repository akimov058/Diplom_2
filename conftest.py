import pytest
import requests
from faker import Faker

@pytest.fixture()
def generate_random_email():
    email = Faker.email(locale="ru_RU")
    return email

@pytest.fixture()
def generate_random_password():
    password = Faker.password(length=10)
    return password

@pytest.fixture()
def generate_random_name():
    name = Faker.name(locale="ru_RU")
    return name