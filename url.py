class URL:
    BASE_URL = "https://stellarburgers.education-services.ru/"

    # Регистрация пользователя
    REGISTRATION_USER_ENDPOINT = f"{BASE_URL}api/auth/register"  # POST
    # Авторизация пользователя
    LOGIN_USER_ENDPOINT = f"{BASE_URL}api/auth/login"  # POST
    # Удалить пользователя
    DELETE_USER_ENDPOINT = f"{BASE_URL}api/auth/user"  # DELETE

    # Получение данных об ингредиентах
    GET_INGREDIENTS_ENDPOINT = f"{BASE_URL}api/ingredients"  # GET
    # Создание заказа
    CREATE_ORDER_ENDPOINT = f"{BASE_URL}api/orders"  # POST
