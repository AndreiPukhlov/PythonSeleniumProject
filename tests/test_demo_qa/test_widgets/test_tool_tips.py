from data.urls.demoqa_urls import DemoqaUrls
from pages.demoqa_pages.demo_qa_homepage import DemoqaHomePage
from pages.demoqa_pages.widgets_page import WidgetPage
from pages.demoqa_pages.widgets_pages.tool_tips_page import ToolTipsPage


class TestToolTips:
    url = DemoqaUrls()

    def test_hover_me_button_tool_tip(self, driver):
        page = DemoqaHomePage(driver, self.url.base_url)
        page.open()
        page.go_to_widgets()
        WidgetPage(driver, '').go_to_tool_tips()
        page = ToolTipsPage(driver, '')
        page.hover_over_button()
        assert page.is_tool_tip_visible()
