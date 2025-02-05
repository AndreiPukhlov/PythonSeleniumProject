from locators.input_page_locators import InputPageLocators
from pages.base_page import BasePage


class InputsPage(BasePage):
    locators = InputPageLocators()

    def enter_number(self, number):
        self.element_is_visible(self.locators.INPUT_FIELD).send_keys(number)

    def get_value(self):
        return self.element_is_visible(self.locators.INPUT_FIELD).get_attribute("value")
