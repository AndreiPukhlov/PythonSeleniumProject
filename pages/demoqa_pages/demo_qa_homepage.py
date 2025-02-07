import time

from locators.demoqa_locators.demoqa_homepage_locators import DemoqaHomePageLocators
from pages.base_page import BasePage


class DemoqaHomePage(BasePage):
    hp_locators = DemoqaHomePageLocators()

    def go_to_elements(self):
        self.element_is_clickable(self.hp_locators.ELEMENTS_BUTTON).click()

    def go_to_forms(self):
        self.element_is_clickable(self.hp_locators.FORMS_BUTTON).click()

    def go_to_widgets(self):
        self.element_is_clickable(self.hp_locators.WIDGETS_BUTTON).click()

