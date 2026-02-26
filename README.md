## Тестирование API сервиса Яндекс Самокат

1. Основа для написания автотестов — фреймворк Pytest.
2. Библитека для генерации отчёта Allure.
2. Установить зависимости:
— pip3 install -r requirements.txt
— pip install -r requirements.txt (если Python второй версии)

Проведённые тесты:
- Регистрация пользователя test_create_user
    - test_create_user_success
    - test_create_user_with_existing_login_returns_error
    - test_create_user_one_fields_missing_returns_error
- Авторизация пользователя test_login_user
    - test_login_user_success
    - test_no_exist_login_or_password_returns_error
- Создание заказа test_create_order
    - test_create_order_with_registered_user_success
    - test_create_order_with_unregistered_user_success
    - test_create_order_without_ingredients_return_error
    - test_create_order_with_incorrect_hash_ingredients_return_error