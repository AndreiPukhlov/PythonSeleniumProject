from locators.alert_page_locators import AlertPageLocators
from pages.base_page import BasePage


class AlertPage(BasePage):
    locators = AlertPageLocators()

    def get_alert_result_text(self):
        return self.element_is_visible(self.locators.ALERT_RESULT_TEST).text

    def alert_confirm(self, alert):
        self.alert_accept(alert)

    def click_button_for_alert(self, button_for_alert_locator):
        self.element_is_clickable(button_for_alert_locator).click()
        self.alert_is_visible()
        alert = self.driver.switch_to.alert
        return alert
