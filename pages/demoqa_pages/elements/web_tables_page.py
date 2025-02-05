from locators.demoqa_locators.elements_locators.web_tables_locators import WebTablesLocators
from pages.base_page import BasePage


class WebTablesPage(BasePage):
    locators = WebTablesLocators()

    def click_add_emp_button(self):
        self.element_is_visible(self.locators.ADD_BUTTON).click()

    def is_open_modal_window(self):
        return self.element_is_visible(self.locators.MODAL_WINDOW).is_displayed()

    def click_x_button(self):
        self.element_is_clickable(self.locators.MODAL_WINDOW_CLOSE_BUTTON).click()

    def close_modal_window_by_empty_space_click(self):
        self.element_is_clickable(self.locators.MODAL_WINDOW_CLOSE_BUTTON).click()

    def is_not_open_modal_window(self):
        return self.element_is_invisible(self.locators.MODAL_WINDOW)

    def input_info(self, locator, text):
        self.element_is_visible(locator).send_keys(text)

    def clear_info(self, locator):
        self.element_is_visible(locator).clear()

    def submit_web_form(self):
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    def type_search(self, last_name):
        self.element_is_visible(self.locators.TYPE_TO_SEARCH_FIELD).send_keys(last_name)

    def get_new_employee(self, last_name):
        self.type_search(last_name)
        return self.elements_are_visible(self.locators.WEB_TABLE)

    def edit_search_result_form(self, email):
        locator = ("xpath", f"//div[text()='{email}']/following-sibling::*//*[@class='action-buttons']/span["
                            f"@id='edit-record-4']")
        self.element_is_clickable(locator).click()

    def clean_search_field(self):
        self.element_is_visible(self.locators.TYPE_TO_SEARCH_FIELD).clear()

    def delete_search_result_form(self, email):
        locator = ("xpath", f"//div[text()='{email}']/following-sibling::*//*[@class='action-buttons']/span["
                            f"@id='delete-record-4']")
        self.element_is_clickable(locator).click()

    def is_employee_deleted(self, email):
        locator = ("xpath", f"//*[text()='{email}']")
        self.type_search(email)
        return self.element_is_invisible(locator)
