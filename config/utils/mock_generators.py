import random
from faker import Faker
from typing import Dict, List, Union

fake = Faker()


class MockGenerator:
    """Генератор тестовых данных"""

    @staticmethod
    def user(role: str = "customer") -> Dict[str, Union[str, bool]]:
        """Генерирует данные пользователя"""
        return {
            "username": fake.user_name(),
            "password": fake.password(length=12),
            "email": fake.email(),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "is_active": True,
            "role": role,
            "phone": fake.phone_number()}

    @staticmethod
    def address() -> Dict[str, str]:
        """Генерирует адрес"""
        return {
            "street": fake.street_address(),
            "city": fake.city(),
            "zip_code": fake.zipcode(),
            "country": fake.country()}