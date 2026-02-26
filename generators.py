from faker import Faker


fake_en = Faker('ru_RU')

def generate_user_body():
    return {
        "email": fake_en.email(),
        "password": fake_en.password(),
        "name": fake_en.name()
    }
