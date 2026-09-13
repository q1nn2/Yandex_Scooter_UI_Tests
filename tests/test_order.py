import allure
import pytest

from data import OrderData
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature("Заказ самоката")
class TestOrder:

    @allure.title("Успешный заказ через точку входа: {entry_point}")
    @pytest.mark.parametrize(
        "entry_point, order_data",
        OrderData.CASES,
    )
    def test_successful_order(
        self,
        driver,
        entry_point,
        order_data,
    ):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open_main_page()
        main_page.close_cookie_banner()

        if entry_point == "top":
            main_page.click_order_button_top()
        elif entry_point == "bottom":
            main_page.click_order_button_bottom()
        else:
            raise ValueError(
                f"Неизвестная точка входа: {entry_point}"
            )

        order_page.create_order(order_data)
        success_message = order_page.get_success_message()

        assert "Заказ оформлен" in success_message
