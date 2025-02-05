import time

import pytest

from data.test_data.input_data import InputData
from data.urls.url import Urls
from pages.inputs_page import InputsPage
from functions import random_number


class TestInputs:
    url = Urls()
    test_data = InputData()

    def test_input_number(self, driver):
        page = InputsPage(driver, f"{self.url.base_url}{self.url.inputs_url}")
        page.open()
        number = random_number()
        page.enter_number(number)
        assert page.get_value() == str(number)

    @pytest.mark.parametrize("enter", test_data.INVALID_DATA)
    def test_input_string(self, driver, enter):
        page = InputsPage(driver, f"{self.url.base_url}{self.url.inputs_url}")
        page.open()
        page.enter_number(enter)
        assert page.get_value() == ''
