from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.webkitgtk.webdriver import WebDriver


class BasePage:

    def __init__(self, driver: WebDriver, url: str, timeout: int = 25):
        self.driver = driver
        self.url = url
        self.action = ActionChains(self.driver)
        self.timeout = timeout

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=None):
        return wait(self.driver, timeout or self.timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=None):
        return wait(self.driver, timeout or self.timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_clickable(self, locator, timeout=None):
        return wait(self.driver, timeout or self.timeout).until(EC.element_to_be_clickable(locator))

    def element_is_invisible(self, locator, timeout=None):
        return wait(self.driver, timeout or self.timeout).until(EC.invisibility_of_element(locator))

    def element_is_present(self, locator, timeout=None):
        return wait(self.driver, timeout or self.timeout).until(EC.presence_of_element_located(locator))

    def alert_is_visible(self, timeout=None):
        wait(self.driver, timeout or self.timeout).until(EC.alert_is_present())

    def double_click(self, element):
        self.action.double_click(element).perform()

    def right_click(self, element):
        self.action.context_click(element).perform()

    def click_with_js(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', "
                                   "inline: 'nearest'});", element)

    def select_by_text(self, locator, txt):
        Select(self.element_is_visible(locator)).select_by_visible_text(txt)

    def get_element_by_locator(self, locator):
        return self.element_is_visible(locator)

    def get_window_handles(self):
        return self.driver.window_handles

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




