
from data.test_data.alert_page_test_data import AlertPageTestData
from data.urls.url import Urls
from locators.alert_page_locators import AlertPageLocators
from pages.alert_page import AlertPage


class TestAlert:
    url = Urls()
    alert_data = AlertPageTestData()
    locators = AlertPageLocators()

    def test_alert(self, driver):
        page = self.open_alert_page(driver)
        alert = page.click_button_for_alert(self.locators.CLICK_ALERT)
        assert page.get_alert_text(alert) == self.alert_data.ALERT_TEXT

    def test_alert_result_text(self, driver):
        page = self.open_alert_page(driver)
        alert = page.click_button_for_alert(self.locators.CLICK_ALERT)
        page.alert_accept(alert)
        assert page.get_alert_result_text() == self.alert_data.ALERT_CLICK_RESULT_TEXT

    def test_confirm_alert(self, driver):
        page = self.open_alert_page(driver)
        alert = page.click_button_for_alert(self.locators.CONFIRM_ALERT)
        assert page.get_alert_text(alert) == self.alert_data.ALERT_CONFIRM_TEXT
        page.alert_accept(alert)

    def test_alert_confirmed_result_text(self, driver):
        page = self.open_alert_page(driver)
        alert = page.click_button_for_alert(self.locators.CONFIRM_ALERT)
        page.alert_confirm(alert)
        assert page.get_alert_result_text() == self.alert_data.ALERT_CONFIRM_RESULT_TEXT

    def test_dismiss_alert(self, driver):
        page = self.open_alert_page(driver)
        alert = page.click_button_for_alert(self.locators.CONFIRM_ALERT)
        assert page.get_alert_text(alert) == self.alert_data.ALERT_CONFIRM_TEXT

    def test_alert_dismissed_result_text(self, driver):
        page = self.open_alert_page(driver)
        alert = page.click_button_for_alert(self.locators.CONFIRM_ALERT)
        page.alert_dismiss(alert)
        assert page.get_alert_result_text() == self.alert_data.ALERT_DISMISS_RESULT_TEXT

    def test_prompt_alert_ok(self, driver):
        page = self.open_alert_page(driver)
        alert = page.click_button_for_alert(self.locators.PROMPT_ALERT)
        page.alert_send_prompt(alert, self.alert_data.PROMPT_TXT)
        page.alert_accept(alert)
        assert page.get_alert_result_text() == f"You entered: {self.alert_data.PROMPT_TXT}"

    def test_prompt_alert_cancel(self, driver):
        page = self.open_alert_page(driver)
        alert = page.click_button_for_alert(self.locators.PROMPT_ALERT)
        page.alert_send_prompt(alert, self.alert_data.PROMPT_TXT)
        page.alert_dismiss(alert)
        assert page.get_alert_result_text() == f"You entered: null"

    def open_alert_page(self, driver):
        alert_url = f"{self.url.base_url}{self.url.alert_page_url}"
        page = AlertPage(driver, alert_url)
        page.open()
        assert driver.current_url == self.url.base_url + self.url.alert_page_url
        return page
