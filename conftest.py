import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    browser = webdriver.Firefox(options=options)
    browser.set_window_size(1440, 1000)

    yield browser

    browser.quit()
