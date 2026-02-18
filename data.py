class DataForUser:
    email = None
    password = None
    name = None

    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name

    @property
    def create_user_body(self):
        return {
            "email": self.email,
            "password": self.password,
            "name": self.name
        }
    
    @property
    def login_user_body(self):
        return {
            "email": self.email,
            "password": self.password
        }

class DataForOrder:
    _ingredients = []

    def __init__(self, ingredient):
        self._ingredients = ingredient
    
    @property
    def create_order_body(self):
        return {
            "ingredients": self._ingredients
        }


class ExpectedValueForRegistrationUser:
    expected_body_successfully_registration_user = True
    expected_body_exists_user = {"success": False, "message": "User already exists"}
    expected_body_one_fields_missing = {"success": False, "message": "Email, password and name are required fields"}

class ExpectedValueForLoginUser:
    expected_body_missing_login_or_password = {"success": False, "message": "email or password are incorrect"}

class ExpectedValueForLogoutUser:
    expected_body_logout_user = {"success": True,"message":"Successful logout"}

class ExpectedValueForCreateOrder:
    expected_body_successfully_create_order_with_logged_user = True
    expected_body_without_ingredients = {"success": False, "message": "Ingredient ids must be provided"}
