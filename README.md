## Тестирование API сервиса "Stellar Burgers"

#### Стэк: Requests, PyTest, Allure, Allure-report, Faker.
Также было протестировано API вручную в Postman.

## Проведённые тесты:
#### - Регистрация пользователя в модуле _test_create_user_:
**test_create_user_success** - проверка успешного создания пользователя\
**test_create_user_with_existing_login_returns_error** - проверка создания пользователя, который уже зарегистрирован\
**test_create_user_one_fields_missing_returns_error** - проверка на невозможность зарегистрироваться пользователю, если нет обязательного поля

#### - Авторизация пользователя в модуле _test_login_user_:
**test_login_user_success** - проверка успешной авторизации пользователя\
**test_no_exist_login_or_password_returns_error** - проверка на невозможность авторизации с несуществующей парой логин-пароль

#### - Создание заказа в модуле _test_create_order_:
**test_create_order_with_registered_user_success** - проверка успешного создания заказа, если пользователь авторизован\
**test_create_order_with_unregistered_user_success** - проверка успешного создания заказа, если пользователь не авторизован\
**test_create_order_without_ingredients_return_error** - проверка на невозможность создания заказа без ингредиентов\
**test_create_order_with_incorrect_hash_ingredients_return_error** - проверка на невозможность создания заказа с несуществующим хешем ингредиенто

  ## Установка зависимостей:
```
pip3 install -r requirements.txt
```
##### Для Python второй версии:
```
pip install -r requirements.txt
```
## Посмотреть отчёт в формате веб-страницы:
```
allure serve allure_results
```
