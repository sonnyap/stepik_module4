import os
import random

from helpers.data_structures import UserRegistration


def get_full_path(file_name: str) -> str:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    relative_path = f"constants/{file_name}"
    return os.path.join(current_dir, relative_path)


def load_data(file_name: str, data_class):
    full_path = get_full_path(file_name)
    return data_class.from_json(full_path)


class UserRegistrationData:
    user_data = load_data("register_data.json", UserRegistration)
    random_email = f"stepik-test-{random.randint(1000000, 100000000)}@test.com"
    random_passwrod = f"test-{random.randint(1000000, 100000000)}"
    user_data = user_data._replace(email=random_email)
    user_data = user_data._replace(password=random_passwrod)
