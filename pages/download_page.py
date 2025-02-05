from locators.download_page_locators import DownloadPageLocators
from pages.base_page import BasePage


class DownloadPage(BasePage):
    locators = DownloadPageLocators()

    def download_file(self):
        self.element_is_visible(self.locators.SNAPCHAT_LINK).click()
