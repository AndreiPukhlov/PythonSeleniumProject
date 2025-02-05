import random
import functions


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
