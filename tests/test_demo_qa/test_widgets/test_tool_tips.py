from data.test_data.demoqa_testdata.widgets_testdata.tool_tips_testdata import ToolTipsTestdata
from data.urls.demoqa_urls import DemoqaUrls
from pages.demoqa_pages.demo_qa_homepage import DemoqaHomePage
from pages.demoqa_pages.widgets_page import WidgetPage
from pages.demoqa_pages.widgets_pages.tool_tips_page import ToolTipsPage


class TestToolTips:
    url = DemoqaUrls()
    testdata = ToolTipsTestdata()

    def test_hover_me_button_tool_tip(self, driver):
        page = DemoqaHomePage(driver, self.url.base_url)
        page.open()
        page.go_to_widgets()
        WidgetPage(driver, '').go_to_tool_tips()
        page = ToolTipsPage(driver, '')
        page.hover_over_button()
        assert page.is_tool_tip_visible()

    def test_cursor_changed_to_pointer(self, driver):
        page = self.go_to_tool_tips_page(driver)
        page.hover_over_button()
        property_value = page.get_cursor_value()
        assert property_value == "pointer", "Cursor did not change to pointer!"

    def test_button_background_color_changes(self, driver):
        page = self.go_to_tool_tips_page(driver)
        before_background_color = page.get_button_background_color()
        page.hover_over_button()
        after_background_color = page.get_button_background_color()
        assert before_background_color != after_background_color
        assert before_background_color == self.testdata.button_background_color
        assert after_background_color == self.testdata.button_background_color_after_hover_over

    def go_to_tool_tips_page(self, driver):
        expected_url = self.url.base_url + self.url.tool_tips_page_url
        page = ToolTipsPage(driver, expected_url)
        page.open()
        assert driver.current_url == expected_url
        return page
