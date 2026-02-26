import requests
import allure

from url import *


class OrderMethods:
    @staticmethod
    def create_order(body, access_token=''):
        with allure.step('Создать заказ'):
            headers = {'Authorization': access_token}
            return requests.post(url=URL.CREATE_ORDER_ENDPOINT, json=body, headers=headers)
    
    @staticmethod
    def get_ingredients():
        with allure.step('Получить ингредиенты'):
            return requests.get(url=URL.GET_INGREDIENTS_ENDPOINT)
