import pytest

from data import DataForUser, DataForOrder
from generators import generate_user_body
from methods.user_methods import UserMethods, delete_test_user
from methods.order_methods import OrderMethods


@pytest.fixture()
def user_body(delete_test_user=delete_test_user):
    body = generate_user_body()
    user = DataForUser(email=body['email'], password=body['password'], name=body['name'])

    yield user

    delete_test_user(user=user)

@pytest.fixture()
def create_user(user_body):
    user = user_body
    UserMethods.registration_user(user.create_user_body)

    yield user

@pytest.fixture()
def access_token_user(create_user):
    user = create_user
    response = UserMethods.login_user(user.login_user_body)
    access_token = response.json()['accessToken']

    yield access_token

@pytest.fixture()
def order_body():
    response_ingredients = OrderMethods.get_ingredients()
    ingredients = response_ingredients.json()['data']
    ingredients = [ingredient['_id'] for i, ingredient in enumerate(ingredients) if i < 3]

    order = DataForOrder(ingredients)

    yield order
