import allure

from data import OrderData
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature("Заказ самоката")
class TestOrder:

    @allure.title("Успешный заказ через верхнюю кнопку «Заказать»")
    def test_successful_order_from_top_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        order_data = OrderData.CASES[0][1]

        main_page.open_main_page()
        main_page.close_cookie_banner()
        main_page.click_order_button_top()

        order_page.create_order(order_data)
        success_message = order_page.get_success_message()

        assert "Заказ оформлен" in success_message

    @allure.title("Успешный заказ через нижнюю кнопку «Заказать»")
    def test_successful_order_from_bottom_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        order_data = OrderData.CASES[1][1]

        main_page.open_main_page()
        main_page.close_cookie_banner()
        main_page.click_order_button_bottom()

        order_page.create_order(order_data)
        success_message = order_page.get_success_message()

        assert "Заказ оформлен" in success_message
