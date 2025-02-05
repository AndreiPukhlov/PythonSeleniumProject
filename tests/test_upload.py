import pytest

from data.test_data.upload_page_test_data import UploadTestData
from data.urls.url import Urls
from pages.upload_page import UploadPage


class TestUpload:
    url = Urls()
    test_data = UploadTestData()

    @pytest.mark.parametrize("file_name", test_data.FILE_LIST_PARAMETRIZE)
    def test_upload(self, driver, file_name):
        page = UploadPage(driver, f"{self.url.base_url}{self.url.upload_page_url}")
        page.open()
        page.upload_file(file_name)
        h3_text, file_name = page.check_uploaded_file()
        assert h3_text == self.test_data.H3_TEXT
        assert file_name == file_name
