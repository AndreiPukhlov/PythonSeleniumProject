import time
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

    def test_web_form_submission_all_fields(self, driver):

        gd = self.generator.generate_employee_data()
        gender = self.generator.generate_random_gender()
        mobile = functions.get_random_mobile_number()
        hobby = self.generator.generate_random_hobby()
        address = self.generator.generate_random_address()
        picture = WebFormTestData.file_path
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
        # page.pick_birthday(dob) # TODO AP:    ADD DOB PICKER METHOD
        page.scroll_to_element()
        page.enter_subject(gd[5])
        page.check_hobby(hobby)
        page.upload_file(picture)
        assert page.uploaded_file_result() == picture
        page.enter_address(address)
        page.select_state(state)
        page.select_city(city)
        page.submit_form()

        submitted_info = page.get_info_submitted()
        submission = [submitted_info[i].text for i in range(len(submitted_info)) if i % 2 != 0]
        exp_data = [
            gd[0] + ' ' + gd[1],
            gd[3],
            gender,
            str(mobile),
            '04 February,2025',
            '',
            hobby,
            picture,
            address,
            (state + " " + city)]
        assert submission == exp_data, f"Expected: {exp_data}\nActual: {submission}"

    def test(self, driver):
        page = PracticeWebFormPage(driver, '')
        page.upload_file("cat.jpg")
