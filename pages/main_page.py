import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from data import Urls


class MainPage(BasePage):
    ORDER_BUTTON_TOP = (
        By.XPATH,
        "//div[contains(@class,'Header_Nav')]//button[text()='Заказать']"
    )
    ORDER_BUTTON_BOTTOM = (
        By.XPATH,
        "//div[contains(@class,'Home_FinishButton')]//button[text()='Заказать']"
    )

    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    SCOOTER_LOGO = (
        By.XPATH,
        "//a[contains(@class,'Header_LogoScooter')]"
    )
    YANDEX_LOGO = (
        By.XPATH,
        "//a[contains(@class,'Header_LogoYandex')]"
    )

    @staticmethod
    def question_locator(index):
        return By.ID, f"accordion__heading-{index}"

    @staticmethod
    def answer_locator(index):
        return By.ID, f"accordion__panel-{index}"

    @allure.step("Открыть главную страницу сервиса")
    def open_main_page(self):
        self.open(Urls.MAIN_PAGE)

    @allure.step("Закрыть cookie-баннер, если он отображается")
    def close_cookie_banner(self):
        try:
            button = self.wait.until(
                EC.element_to_be_clickable(self.COOKIE_BUTTON)
            )
            button.click()
        except TimeoutException:
            pass

    @allure.step("Нажать верхнюю кнопку «Заказать»")
    def click_order_button_top(self):
        self.click(self.ORDER_BUTTON_TOP)

    @allure.step("Нажать нижнюю кнопку «Заказать»")
    def click_order_button_bottom(self):
        self.scroll_to(self.ORDER_BUTTON_BOTTOM)
        self.click(self.ORDER_BUTTON_BOTTOM)

    @allure.step("Открыть вопрос №{index}")
    def open_question(self, index):
        locator = self.question_locator(index)
        self.scroll_to(locator)
        self.click(locator)

    @allure.step("Получить ответ на вопрос №{index}")
    def get_answer(self, index):
        locator = self.answer_locator(index)
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).text

    @allure.step("Нажать на логотип «Самокат»")
    def click_scooter_logo(self):
        self.click(self.SCOOTER_LOGO)

    @allure.step("Нажать на логотип Яндекса и перейти в новое окно")
    def click_yandex_logo_and_switch(self):
        old_windows = set(self.driver.window_handles)
        self.click(self.YANDEX_LOGO)

        self.wait.until(
            lambda driver: len(set(driver.window_handles) - old_windows) == 1
        )
        new_window = (set(self.driver.window_handles) - old_windows).pop()
        self.driver.switch_to.window(new_window)
        self.wait.until(EC.url_contains("dzen.ru"))
