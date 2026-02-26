import pytest
import allure

from data import ExpectedValueForLoginUser as EVLoginUser
from methods.user_methods import UserMethods


class TestLoginUser:
    @allure.title('Проверка успешной авторизации пользователя')
    @allure.description('Проверяется тело и код ответа')
    def test_login_user_success(self, create_user):
        body = create_user.login_user_body
        
        response = UserMethods.login_user(body)

        assert response.status_code == 200
        assert "accessToken" in response.json()
    
    @allure.title('Проверка на невозможность авторизации с несуществующей парой логин-пароль')
    @allure.description('Проверяется тело и код ответа')
    @pytest.mark.parametrize('key1, key2', [('email', 'password'), ('password', 'email')])
    def test_no_exist_login_or_password_returns_error(self, create_user, key1, key2):
        body = create_user.login_user_body
        body[key1] = body[key2]
        
        response = UserMethods.login_user(body)

        assert response.status_code == 401
        assert response.json() == EVLoginUser.expected_body_missing_login_or_password
