from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.webkitgtk.webdriver import WebDriver


class BasePage:

    def __init__(self, driver: WebDriver, url: str):
        self.driver = driver
        self.url = url
        self.action = ActionChains(self.driver)

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=20):
        return wait(self.driver, timeout=timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=20):
        return wait(self.driver, timeout=timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_clickable(self, locator, timeout=20):
        return wait(self.driver, timeout=timeout).until(EC.element_to_be_clickable(locator))

    def element_is_invisible(self, locator, timeout=20):
        return wait(self.driver, timeout=timeout).until(EC.invisibility_of_element(locator))

    def element_is_present(self, locator, timeout=20):
        return wait(self.driver, timeout=timeout).until(EC.presence_of_element_located(locator))

    def alert_is_visible(self, timeout=20):
        wait(self.driver, timeout=timeout).until(EC.alert_is_present())

    def double_click(self, element):
        self.action.double_click(element).perform()

    def right_click(self, element):
        self.action.context_click(element).perform()

    @staticmethod
    def get_alert_text(alert):
        alert_text = alert.text
        return alert_text

    @staticmethod
    def alert_accept(alert):
        alert.accept()

    @staticmethod
    def alert_send_prompt(alert, prompt):
        alert.send_keys(prompt)

    @staticmethod
    def alert_dismiss(alert):
        alert.dismiss()
