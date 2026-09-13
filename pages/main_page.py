import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from data import Urls
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Открыть главную страницу сервиса")
    def open_main_page(self):
        self.open(Urls.MAIN_PAGE)

    @allure.step("Закрыть cookie-баннер, если он отображается")
    def close_cookie_banner(self):
        try:
            button = self.wait.until(
                EC.element_to_be_clickable(MainPageLocators.COOKIE_BUTTON)
            )
            button.click()
        except TimeoutException:
            pass

    @allure.step("Нажать верхнюю кнопку «Заказать»")
    def click_order_button_top(self):
        self.click(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step("Нажать нижнюю кнопку «Заказать»")
    def click_order_button_bottom(self):
        self.scroll_to(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.click(MainPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step("Открыть вопрос №{index}")
    def open_question(self, index):
        locator = MainPageLocators.question(index)
        self.scroll_to(locator)
        self.click(locator)

    @allure.step("Получить ответ на вопрос №{index}")
    def get_answer(self, index):
        locator = MainPageLocators.answer(index)
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).text

    @allure.step("Нажать на логотип «Самокат»")
    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Нажать на логотип Яндекса и перейти в новое окно")
    def click_yandex_logo_and_switch(self):
        old_windows = set(self.driver.window_handles)
        self.click(MainPageLocators.YANDEX_LOGO)

        self.wait.until(
            lambda driver: len(set(driver.window_handles) - old_windows) == 1
        )
        new_window = (set(self.driver.window_handles) - old_windows).pop()
        self.driver.switch_to.window(new_window)
        self.wait.until(EC.url_contains("dzen.ru"))
