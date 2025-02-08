from locators.demoqa_locators.widgets_locators.tool_tips_locators import ToolTipsLocators
from pages.base_page import BasePage


class ToolTipsPage(BasePage):

    locator = ToolTipsLocators()

    def hover_over_button(self):
        element = self.element_is_clickable(self.locator.HOVER_ME_BUTTON)
        self.action.move_to_element(element).perform()

    def is_tool_tip_visible(self):
        return self.element_is_visible(self.locator.HOVER_ME_BUTTON_TOOL_TIP)

    def get_cursor_value(self):
        return self.get_css_property(self.locator.HOVER_ME_BUTTON, "cursor")

    def get_button_background_color(self):
        return self.get_css_property(self.locator.HOVER_ME_BUTTON, "background-color")

