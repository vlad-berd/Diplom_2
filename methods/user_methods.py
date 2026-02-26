import requests
import allure

from url import *


class UserMethods:
    @staticmethod
    def registration_user(body):
        with allure.step('Зарегистрировать пользователя'):
            return requests.post(URL.REGISTRATION_USER_ENDPOINT, json=body)

    @staticmethod
    def login_user(body):
        with allure.step('Авторизовать пользователя'):
            return requests.post(URL.LOGIN_USER_ENDPOINT, json=body)
    
    @staticmethod
    def delete_user(access_token):
        with allure.step('Удалить пользователя'):
            headers = {'Authorization': access_token}
            return requests.delete(URL.DELETE_USER_ENDPOINT, headers=headers)


def delete_test_user(user):
    with allure.step('Получение token пользователя для удаления тестового пользователя'):
        response_login = UserMethods.login_user(user.login_user_body)

        if response_login.status_code == 200:
            access_token = response_login.json()['accessToken']

            with allure.step('Удаление тестового курьера'):
                UserMethods.delete_user(access_token=access_token)
