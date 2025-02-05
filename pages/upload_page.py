import time

from functions import get_root_path
from locators.upload_page_locators import UploadPageLocators
from pages.base_page import BasePage


class UploadPage(BasePage):
    locators = UploadPageLocators()

    def upload_file(self, file):
        file_path = get_root_path(self.locators.UPLOAD_FOLDER_PATH + file)
        print(file_path)
        self.element_is_visible(self.locators.CHOOSE_FILE_BUTTON).send_keys(file_path)
        self.element_is_clickable(self.locators.UPLOAD_BUTTON).click()

    def check_uploaded_file(self):
        h3_text = self.element_is_visible(self.locators.HEADER_TEXT).text
        file_name = self.element_is_visible(self.locators.UPLOADED_FILE_NAME_LOCATOR).text
        return h3_text, file_name
