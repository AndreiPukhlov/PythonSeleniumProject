import time
from datetime import date

import pytest
import functions
from data.data_generators.employee_info_generator import EmployeeIngoGenerator
from data.test_data.demoqa_testdata.web_form_test_data import WebFormTestData
from data.urls.demoqa_urls import DemoqaUrls
from pages.demoqa_pages.demo_qa_homepage import DemoqaHomePage
from pages.demoqa_pages.demoqa_web_forms_page import WebFormsPage
from pages.demoqa_pages.web_forms.practice_web_forms_page import PracticeWebFormPage


class TestWebForm:
    url = DemoqaUrls()
    generator = EmployeeIngoGenerator()

    @pytest.mark.parametrize("run", range(5))  # Runs the tess n times
    @pytest.mark.smoke
    def test_web_form_submission_all_fields(self, driver, run):
        gd = self.generator.generate_employee_data()
        gender = self.generator.generate_random_gender()
        mobile = functions.get_random_mobile_number()
        hobby = self.generator.generate_random_hobby()
        address = self.generator.generate_random_address()
        picture = WebFormTestData.file_path
        year, month, day = self.generator.dob_generator()
        state, city = self.generator.generate_random_state_city()

        page = DemoqaHomePage(driver, self.url.base_url)
        page.open()
        page.go_to_forms()
        WebFormsPage(driver, "").go_to_practice_web_forms()
        page = PracticeWebFormPage(driver, "")
        exp_url = self.url.base_url + self.url.practice_web_form_url
        assert page.driver.current_url == exp_url, f"Expected {exp_url}, \nbut got {driver.current_url}"
        page.enter_firstname(gd[0])
        page.enter_lastname(gd[1])
        page.enter_email(gd[3])
        page.choose_gender(gender)
        page.enter_mobile_number(mobile)
        page.pick_birthday(day, month, year)
        page.scroll_to_element()
        page.enter_subject(gd[5])
        page.check_hobby(hobby)
        page.upload_file(picture)
        assert page.uploaded_file_result() == picture
        page.enter_address(address)
        page.select_state(state)
        page.select_city(city)
        page.submit_form()

        if len(str(day)) == 1:
            day = '0' + str(day)
        formatted_date = f"{day} {month},{year}"

        submitted_info = page.get_info_submitted()
        submission = [submitted_info[i].text for i in range(len(submitted_info)) if i % 2 != 0]
        exp_data = [
            gd[0] + ' ' + gd[1],
            gd[3],
            gender,
            str(mobile),
            formatted_date,
            '',
            hobby,
            picture,
            address,
            (state + " " + city)]

        assert submission == exp_data, f"Expected: {exp_data}\nActual: {submission}"
        page.close_modal_window()
        assert page.is_modal_window_closed()

    @pytest.mark.parametrize("run", range(5))  # Runs the test n times
    def test_web_form_submission_required_fields(self, driver, run):
        gd = self.generator.generate_employee_data()
        gender = self.generator.generate_random_gender()
        mobile = functions.get_random_mobile_number()
        today = date.today()
        formatted_date = today.strftime("%d %B,%Y")

        exp_url = self.url.base_url + self.url.practice_web_form_url
        page = PracticeWebFormPage(driver, exp_url)
        page.open()
        assert page.driver.current_url == exp_url, f"Expected {exp_url}, \nbut got {driver.current_url}"
        page.enter_firstname(gd[0])
        page.enter_lastname(gd[1])
        page.choose_gender(gender)
        page.enter_mobile_number(mobile)
        page.scroll_to_element()

        page.submit_form()
        submitted_info = page.get_info_submitted()
        submission = [submitted_info[i].text for i in range(len(submitted_info)) if i % 2 != 0]
        exp_data = [
            gd[0] + ' ' + gd[1],
            '',
            gender,
            str(mobile),
            formatted_date,
            '',
            '',
            '',
            '',
            '']
        assert submission == exp_data, f"Expected: {exp_data}\nActual: {submission}"
        page.close_modal_window()
        assert page.is_modal_window_closed()
