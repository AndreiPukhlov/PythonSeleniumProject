import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FO

from functions import get_root_path

download_path = get_root_path("data/download")


@pytest.fixture
def driver(request, name="chr"):
    prefs = {
        "download.default_directory": download_path
    }
    if "chr" in name:
        chrome_options = Options()
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--window-size=1920,1080")
        # chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-cache")
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.page_load_strategy = "normal"  # normal eager

        drv = webdriver.Chrome(options=chrome_options)
    elif "saf" in name:
        drv = webdriver.Safari()
        drv.set_window_size(1600, 900)
    elif "fir" in name:
        firefox_options = FO()
        firefox_options.add_argument("--width=1920")
        firefox_options.add_argument("--height=1080")
        firefox_options.add_argument("--incognito")

        drv = webdriver.Firefox(options=firefox_options)
    else:
        pytest.fail("Unknown browser name")

    drv.delete_all_cookies()

    yield drv
    drv.quit()


def ensure_screenshot_dir():
    screenshot_dir = "screenshots"
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)


# pytest --html=report.html --self-contained-html
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    """Hook to take a screenshot on test failure."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshot_path = f"screenshots/{item.name}.png"
            driver.save_screenshot(screenshot_path)
            pytest_html = getattr(item.config, "_html", None)
            if pytest_html:
                extra = getattr(report, "extra", [])
                extra.append(pytest_html.extras.image(screenshot_path))
                report.extra = extra
