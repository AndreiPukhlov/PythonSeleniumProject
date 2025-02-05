from data.test_data.demoqa_testdata.elements_testdata.buttons_testdata import ButtonsTestData
from data.urls.demoqa_urls import DemoqaUrls
from locators.demoqa_locators.demoqa_homepage_locators import DemoqaHomePageLocators
from pages.demoqa_pages.demo_qa_homepage import DemoqaHomePage
from pages.demoqa_pages.elements.buttons_page import ButtonsPage


class TestDemoqaButtons:
    url = DemoqaUrls()
    hp_locators = DemoqaHomePageLocators()
    test_data = ButtonsTestData()

    def test_buttons_page_navigation(self, driver):
        DemoqaHomePage(driver, f"{self.url.base_url}").open()
        home_page = DemoqaHomePage(driver, "")
        home_page.go_to_elements()
        exp_url = self.url.base_url + self.url.elements_url
        assert home_page.driver.current_url == exp_url

    def test_button_double_click(self, driver):
        page = self.go_to_buttons_page(driver)
        page.double_click_button()
        exp_txt = self.test_data.DOUBLE_CLICK_TXT
        assert page.get_double_click_result_text() == exp_txt

    def test_button_right_click(self, driver):
        page = self.go_to_buttons_page(driver)
        page.right_click_button()
        exp_txt = self.test_data.RIGHT_CLICK_TXT
        assert page.get_right_click_result_text() == exp_txt

    def test_dynamic_button_click(self, driver):
        page = self.go_to_buttons_page(driver)
        page.click_dynamic_button()
        exp_txt = self.test_data.DYNAMIC_CLICK_TXT
        assert page.get_dynamic_click_result_text() == exp_txt

    def go_to_buttons_page(self, driver):
        page = ButtonsPage(driver, f"{self.url.base_url}{self.url.buttons_url}")
        page.open()
        exp_url = self.url.base_url + self.url.buttons_url
        assert page.driver.current_url == exp_url
        return page
