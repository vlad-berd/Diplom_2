import pytest
import allure

from data import ExpectedValueForRegistrationUser as EVRegistratioUser
from methods.user_methods import UserMethods


class TestCreateUser:
    @allure.title('Проверка успешного создания пользователя')
    @allure.description('Проверяется тело и код ответа')
    def test_create_user_success(self, user_body):
        body = user_body.create_user_body

        response = UserMethods.registration_user(body)

        assert response.status_code == 200
        assert response.json()['success'] == EVRegistratioUser.expected_body_successfully_registration_user

    @allure.title('Проверка создания пользователя, который уже зарегистрирован')
    @allure.description('Проверяется тело и код ответа')
    def test_create_user_with_existing_login_returns_error(self, user_body):
        body = user_body.create_user_body
        UserMethods.registration_user(body)

        with allure.step('Повторное создания пользователя, который уже зарегистрирован'):
            response = UserMethods.registration_user(body)

        assert response.status_code == 403
        assert response.json() == EVRegistratioUser.expected_body_exists_user

    @allure.title('Проверка на невозможность зарегистрироваться пользователю, если нет обязательного поля {key}')
    @allure.description('Проверяется тело и код ответа')
    @pytest.mark.parametrize('key', ['email', 'password', 'name'])
    def test_create_user_one_fields_missing_returns_error(self, key, user_body):
        body = user_body.create_user_body
        del body[key]

        response = UserMethods.registration_user(body)
        
        assert response.status_code == 403
        assert response.json() == EVRegistratioUser.expected_body_one_fields_missing
    