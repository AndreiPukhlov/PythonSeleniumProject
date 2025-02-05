from locators.demoqa_locators.elements_locators.buttons_locators import ButtonsLocators
from pages.base_page import BasePage


class ButtonsPage(BasePage):

    locators = ButtonsLocators()

    def double_click_button(self):
        element = self.element_is_visible(self.locators.DOUBLE_CLICK_BUTTON)
        self.double_click(element)

    def get_double_click_result_text(self):
        return self.element_is_visible(self.locators.DOUBLE_CLICK_MESSAGE).text

    def right_click_button(self):
        element = self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON)
        self.right_click(element)

    def get_right_click_result_text(self):
        return self.element_is_visible(self.locators.RIGHT_CLICK_MESSAGE).text

    def click_dynamic_button(self):
        self.element_is_visible(self.locators.DYNAMIC_CLICK_BUTTON).click()

    def get_dynamic_click_result_text(self):
        return self.element_is_visible(self.locators.DYNAMIC_CLICK_MESSAGE).text


