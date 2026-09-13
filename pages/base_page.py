import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Открыть страницу {url}")
    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        self.find_clickable(locator).click()

    def type_text(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def scroll_to(self, locator):
        element = self.find(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        return element

    def get_text(self, locator):
        return self.find(locator).text

    def get_current_url(self):
        return self.driver.current_url

    def get_window_handles(self):
        return set(self.driver.window_handles)

    def switch_to_new_window(self, old_windows):
        self.wait.until(
            lambda driver: len(set(driver.window_handles) - old_windows) == 1
        )
        new_window = (set(self.driver.window_handles) - old_windows).pop()
        self.driver.switch_to.window(new_window)

    def wait_for_url_contains(self, value):
        self.wait.until(EC.url_contains(value))
