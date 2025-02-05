from pages.base_page import BasePage


class HoversPage(BasePage):
    def hover_user_avatar(self, user_avatar_id):
        locator = ("xpath", f"(//*[@class='figure'])[{user_avatar_id}]")
        element = self.element_is_visible(locator)
        self.action.move_to_element(element).perform()
