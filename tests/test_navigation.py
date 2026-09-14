import allure

from data import Urls
from pages.main_page import MainPage


@allure.feature("Переходы по логотипам")
class TestNavigation:

    @allure.title("Логотип «Самокат» ведёт на главную страницу")
    def test_scooter_logo_opens_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open(Urls.ORDER_PAGE)

        main_page.click_scooter_logo()

        assert main_page.get_current_url() == Urls.MAIN_PAGE

    @allure.title("Логотип Яндекса открывает главную страницу Дзена")
    def test_yandex_logo_opens_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.close_cookie_banner()

        main_page.click_yandex_logo_and_switch()

        assert Urls.DZEN_DOMAIN in main_page.get_current_url()
