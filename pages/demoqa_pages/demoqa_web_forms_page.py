from locators.demoqa_locators.web_forms_locators.web_forms_locators import WebFormsLocators
from pages.base_page import BasePage


class WebFormsPage(BasePage):

    locator = WebFormsLocators()

    def go_to_practice_web_forms(self):
        self.element_is_visible(self.locator.PRACTICE_FORM_BUTTON).click()