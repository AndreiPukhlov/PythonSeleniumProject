from locators.demoqa_locators.denoqa_elements_page_locators import DemoqaElementsPageLocators
from pages.base_page import BasePage


class DemoqaElementsPage(BasePage):
    elements_locators = DemoqaElementsPageLocators()

    def go_to_buttons(self):
        self.element_is_visible(self.elements_locators.BUTTONS).click()

    def go_to_web_tables(self):
        self.element_is_visible(self.elements_locators.WEB_TABLES).click()
