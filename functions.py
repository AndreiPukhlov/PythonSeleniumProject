import os
import random
from faker import Faker

fake = Faker()


def get_root_path(file_path):
    root_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(root_path, file_path)


def random_number():
    return random.randint(0, 1000)


def get_random_first_name():
    return fake.first_name()


def get_random_last_name():
    return fake.last_name()


def get_random_email():
    return fake.email()


def get_random_department_name():
    return fake.administrative_unit()


def get_random_age():
    return fake.random_int(18, 65)


def get_random_salary():
    return fake.random_int(80000, 180000)


def get_random_mobile_number():
    return fake.random_number(10, True)
