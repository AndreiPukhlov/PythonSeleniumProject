import random
import functions
from datetime import date


class EmployeeIngoGenerator:

    @staticmethod
    def generate_employee_data():
        return [
            functions.get_random_first_name(),
            functions.get_random_last_name(),
            str(functions.get_random_age()),
            functions.get_random_email(),
            str(functions.get_random_salary()),
            functions.get_random_department_name()
        ]

    @staticmethod
    def generate_random_gender():
        gender_list = ["Male", "Female", "Other"]
        random_i = functions.fake.random_int(0, 2)
        return gender_list[random_i]

    @staticmethod
    def generate_random_state_city():
        state_city_map = {
            "Haryana": ["Panipat", "Karnal"],
            "NCR": ["Delhi", "Gurgaon", "Noida"],
            "Uttar Pradesh": ["Agra", "Lucknow", "Merrut"],
            "Rajasthan": ["Jaipur", "Jaiselmer"]
        }

        state = random.choice(list(state_city_map.keys()))
        city = random.choice(state_city_map[state])

        return state, city

    @staticmethod
    def generate_random_hobby():
        hobby_list = ["Sports", "Reading", "Music"]
        random_i = functions.fake.random_int(0, 2)
        return hobby_list[random_i]

    @staticmethod
    def generate_random_address():
        return functions.fake.street_address()

    @staticmethod
    def dob_generator():
        year = random.randint(date.today().year - 120, date.today().year - 18)
        month = functions.fake.month_name()

        days_in_month = {
            "January": 31, "February": 29 if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)) else 28,
            "March": 31, "April": 30, "May": 31, "June": 30,
            "July": 31, "August": 31, "September": 30, "October": 31,
            "November": 30, "December": 31
        }

        day = random.randint(1, days_in_month[month])
        return year, month, day
