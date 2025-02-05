import time

import pytest

from assertions import Assertions
from data.urls.url import Urls
from pages.hovers_page import HoversPage


class TestHover:
    url = Urls()
    assertion = Assertions()

    @pytest.mark.parametrize("user_id", [1, 2, 3])
    def test_user_1_view_profile(self, driver, user_id):
        page = self.open_hover_page(driver)
        page.hover_user_avatar(user_id)
        time.sleep(1)

    def open_hover_page(self, driver):
        page_url = f"{self.url.base_url}{self.url.hovers_url}"
        page = HoversPage(driver, page_url)
        page.open()
        assert driver.current_url == page_url
        return page

