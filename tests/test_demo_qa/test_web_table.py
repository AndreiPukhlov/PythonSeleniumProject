import time

from data.data_generators.employee_info_generator import EmployeeIngoGenerator
from data.test_data.demoqa_testdata.elements_testdata.web_tables_test_data import WebTablesTestData
from data.urls.demoqa_urls import DemoqaUrls
from locators.demoqa_locators.elements_locators.web_tables_locators import WebTablesLocators
from pages.demoqa_pages.demo_qa_homepage import DemoqaHomePage
from pages.demoqa_pages.demoqa_elements_page import DemoqaElementsPage
from pages.demoqa_pages.elements.web_tables_page import WebTablesPage

generator = EmployeeIngoGenerator()


class TestAddWebTable:
    url = DemoqaUrls()
    locators = WebTablesLocators()
    test_data = WebTablesTestData()

    def test_data_check(self):
        data = generator.generate_employee_data()
        print(data)

    def test_add_employee_modal_window_close_with_x_button(self, driver):
        DemoqaHomePage(driver, self.url.base_url).open()
        page = (DemoqaHomePage(driver, ""))
        page.go_to_elements()
        page = (DemoqaElementsPage(driver, ""))
        page.go_to_web_tables()
        page = WebTablesPage(driver, "")
        page.click_add_emp_button()
        assert page.is_open_modal_window()
        page.click_x_button()
        time.sleep(4)
        assert page.is_not_open_modal_window()

    def test_add_employee_window_close_by_click_out_of_the_modal(self, driver):
        page = self.go_to_web_tables(driver)
        page.click_add_emp_button()
        assert page.is_open_modal_window()
        page.close_modal_window_by_empty_space_click()
        assert page.is_not_open_modal_window()

    def go_to_web_tables(self, driver):
        exp_url = self.url.base_url + self.url.web_table_url
        page = WebTablesPage(driver, exp_url)
        page.open()
        assert page.driver.current_url.__eq__(exp_url)
        return page

    def test_create_new_employee(self, driver):
        data, l_name, page = self.create_new_employee(driver)
        time.sleep(0.5)
        new_employee = page.get_new_employee(l_name)
        actual = new_employee[0].text.split('\n')
        assert actual == data, f"Expected {data} but got {actual}"

    def create_new_employee(self, driver):
        page = self.go_to_web_tables(driver)
        page.click_add_emp_button()

        locators = [
            self.locators.FIRST_NAME_FIELD, self.locators.LAST_NAME_FIELD,
            self.locators.AGE_FIELD, self.locators.EMAIL_FIELD,
            self.locators.SALARY_FIELD, self.locators.DEPARTMENT_FIELD
        ]

        data = generator.generate_employee_data()
        for locator, value in zip(locators, data):
            page.input_info(locator, value)
        page.submit_web_form()
        return data, data[1], page

    def test_edit_new_employee(self, driver):
        data, l_name, page = self.create_new_employee(driver)
        time.sleep(0.5)
        email = data[3]
        page.get_new_employee(email)
        page.edit_search_result_form(email)

        new_data = generator.generate_employee_data()

        for locator, value in zip([
            self.locators.FIRST_NAME_FIELD, self.locators.LAST_NAME_FIELD,
            self.locators.AGE_FIELD, self.locators.EMAIL_FIELD,
            self.locators.SALARY_FIELD, self.locators.DEPARTMENT_FIELD
        ], new_data):
            page.clear_info(locator)
            page.input_info(locator, value)

        page.submit_web_form()
        page.clean_search_field()
        edited_employee = page.get_new_employee(new_data[1])
        actual = edited_employee[0].text.split('\n')
        assert actual == new_data, f"Expected {new_data} but got {actual}"

    def test_delete_employee(self, driver):
        data, l_name, page = self.create_new_employee(driver)
        time.sleep(0.5)
        email = data[3]
        page.get_new_employee(email)
        page.delete_search_result_form(email)
        page.clean_search_field()
        time.sleep(6)
        assert page.is_employee_deleted(email)

