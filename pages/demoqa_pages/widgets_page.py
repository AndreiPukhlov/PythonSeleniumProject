from locators.demoqa_locators.widgets_locators.widget_page_locators import WidgetPageLocators
from pages.base_page import BasePage


class WidgetPage(BasePage):

    locator = WidgetPageLocators()

    def go_to_tool_tips(self):
        element = self.element_is_visible(self.locator.TOOLTIP_PAGE_BUTTON)
        self.scroll_to_element(element)
        element.click()



