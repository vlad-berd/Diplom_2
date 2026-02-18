import allure

from methods.order_methods import OrderMethods
from data import ExpectedValueForCreateOrder as EVCreateOrder


class TestCreateOrder:
    @allure.title('Проверка успешного создания заказа, если пользователь авторизован')
    @allure.description('Проверяется тело и код ответа')
    def test_create_order_with_registered_user_success(self, order_body, access_token_user):
        body = order_body.create_order_body

        response = OrderMethods.create_order(body, access_token_user)

        assert response.status_code == 200
        assert response.json()['success'] == EVCreateOrder.expected_body_successfully_create_order_with_logged_user

    @allure.title('Проверка успешного создания заказа, если пользователь не авторизован')
    @allure.description('Проверяется тело и код ответа')
    def test_create_order_with_unregistered_user_success(self, order_body):
        body = order_body.create_order_body

        response = OrderMethods.create_order(body)

        assert response.status_code == 200
        assert response.json()['success'] == EVCreateOrder.expected_body_successfully_create_order_with_logged_user

    @allure.title('Проверка на невозможность создания заказа без ингредиентов')
    @allure.description('Проверяется тело и код ответа')
    def test_create_order_without_ingredients_return_error(self):
        body = {"ingredients": []}

        response = OrderMethods.create_order(body)

        assert response.status_code == 400
        assert response.json() == EVCreateOrder.expected_body_without_ingredients

    @allure.title('Проверка на невозможность создания заказа с несуществующим хешем ингредиенто')
    @allure.description('Проверяется тело и код ответа')
    def test_create_order_with_incorrect_hash_ingredients_return_error(self):
        body = {"ingredients": ["9990c5a71d1f87rz9bdaaa6d"]}

        response = OrderMethods.create_order(body)

        assert response.status_code == 500
