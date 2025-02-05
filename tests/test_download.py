from data.urls.url import Urls
from pages.download_page import DownloadPage


class TestDownload:
    url = Urls()

    def test_download(self, driver):
        download_page_url = f"{self.url.base_url}{self.url.download_page_url}"
        page = DownloadPage(driver, download_page_url)
        page.open()
        assert driver.current_url == download_page_url
        page.download_file()
