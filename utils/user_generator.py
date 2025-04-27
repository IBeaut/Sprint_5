from faker import Faker

fake = Faker()

def generate_email():
    """Генерирует случайный email"""
    return f"{fake.first_name().lower()}{fake.random_int(min=100, max=999)}@yandex.ru"

def generate_password():
    """Генерирует случайный пароль от 6 символов"""
    return fake.password(length=8)
