from selenium.webdriver import Keys

from functions import get_root_path
from locators.demoqa_locators.web_forms_locators.web_forms_locators import WebFormsLocators
from pages.base_page import BasePage


class PracticeWebFormPage(BasePage):
    locator = WebFormsLocators()

    def enter_firstname(self, first_name):
        self.element_is_visible(self.locator.FIRST_NAME).send_keys(first_name)

    def enter_lastname(self, last_name):
        self.element_is_visible(self.locator.LAST_NAME).send_keys(last_name)

    def enter_email(self, email):
        self.element_is_visible(self.locator.EMAIL).send_keys(email)

    def choose_gender(self, gender):
        locator = ("xpath", f"//label[text()='{gender}']")
        self.element_is_visible(locator).click()

    def enter_mobile_number(self, mobile):
        self.element_is_visible(self.locator.MOBILE).send_keys(mobile)

    def enter_subject(self, subject):
        self.element_is_visible(self.locator.SUBJECT).send_keys(subject)

    def check_hobby(self, hobby):
        locator = ("xpath", f"//label[text()='{hobby}']")
        self.element_is_visible(locator).click()

    def enter_address(self, address):
        self.element_is_visible(self.locator.ADDRESS).send_keys(address)

    def submit_form(self):
        self.element_is_visible(self.locator.SUBMIT_BUTTON).click()

    def scroll_to_element(self):
        element = self.element_is_visible(self.locator.ADDRESS)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)

    def get_info_submitted(self):
        return self.elements_are_visible(self.locator.INFO_RESULT)

    def upload_file(self, path):
        file_path = get_root_path(self.locator.UPLOAD_FOLDER_PATH + '/' + path)
        self.element_is_visible(self.locator.CHOOSE_FILE_BUTTON).send_keys(file_path)

    def uploaded_file_result(self):
        return self.element_is_visible(self.locator.CHOOSE_FILE_BUTTON).get_attribute("value").split("\\")[-1]

    def select_state(self, state):
        self.element_is_clickable(self.locator.SELECT_STATE).click()
        element = self.element_is_clickable(self.locator.INPUT_STATE)
        element.send_keys(state)
        element.send_keys(Keys.ENTER)

    def close_modal_window(self):
        self.element_is_visible(self.locator.CLOSE_BUTTON).click()

    def is_modal_window_closed(self):
        return self.element_is_invisible(self.locator.CLOSE_BUTTON)

    def select_city(self, city):
        self.element_is_clickable(self.locator.SELECT_CITY).click()
        element = self.element_is_clickable(self.locator.INPUT_CITY)
        element.send_keys(city)
        element.send_keys(Keys.ENTER)

    def pick_birthday(self, day, month, year):
        year_locator = ("xpath", f"//*[contains(@class,'year')]/option[@value='{year}']")
        month_locator = ("xpath", f"//*[contains(@class,'month')]/option[text()='{month}']")
        day_locator = ("xpath", f"//*[contains(@class, 'day') and not(contains(@class, 'outside'))][text()='{day}']")
        self.element_is_visible(self.locator.DOB_INPUT).click()
        self.element_is_visible(year_locator).click()
        self.element_is_visible(month_locator).click()
        self.element_is_visible(day_locator).click()

