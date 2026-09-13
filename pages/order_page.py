import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step("Заполнить форму «Для кого самокат»")
    def fill_customer_form(self, name, surname, address, metro, phone):
        self.type_text(OrderPageLocators.NAME_INPUT, name)
        self.type_text(OrderPageLocators.SURNAME_INPUT, surname)
        self.type_text(OrderPageLocators.ADDRESS_INPUT, address)

        metro_input = self.find(OrderPageLocators.METRO_INPUT)
        metro_input.click()
        metro_input.send_keys(metro)
        self.click(OrderPageLocators.metro_option(metro))

        self.type_text(OrderPageLocators.PHONE_INPUT, phone)
        self.click(OrderPageLocators.NEXT_BUTTON)

        self.wait.until(
            EC.visibility_of_element_located(
                OrderPageLocators.DELIVERY_DATE_INPUT
            )
        )

    @allure.step("Указать дату доставки: {date}")
    def set_delivery_date(self, date):
        date_input = self.find(OrderPageLocators.DELIVERY_DATE_INPUT)
        date_input.clear()
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)

    @allure.step("Выбрать срок аренды: {period}")
    def select_rent_period(self, period):
        self.click(OrderPageLocators.RENT_PERIOD_DROPDOWN)
        self.click(OrderPageLocators.rent_period_option(period))

    @allure.step("Выбрать цвет самоката: {color}")
    def select_color(self, color):
        if color == "black":
            self.click(OrderPageLocators.BLACK_COLOR)
        elif color == "grey":
            self.click(OrderPageLocators.GREY_COLOR)
        else:
            raise ValueError(f"Неизвестный цвет: {color}")

    @allure.step("Ввести комментарий для курьера")
    def set_comment(self, comment):
        self.type_text(OrderPageLocators.COMMENT_INPUT, comment)

    @allure.step("Заполнить форму «Про аренду»")
    def fill_rent_form(self, date, period, color, comment):
        self.set_delivery_date(date)
        self.select_rent_period(period)
        self.select_color(color)
        self.set_comment(comment)

    @allure.step("Подтвердить заказ")
    def submit_order(self):
        self.scroll_to(OrderPageLocators.ORDER_BUTTON)
        self.click(OrderPageLocators.ORDER_BUTTON)
        self.click(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step("Проверить сообщение об успешном оформлении заказа")
    def get_success_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(OrderPageLocators.SUCCESS_TITLE)
        ).text

    @allure.step("Оформить заказ полностью")
    def create_order(self, order_data):
        self.fill_customer_form(
            order_data["name"],
            order_data["surname"],
            order_data["address"],
            order_data["metro"],
            order_data["phone"],
        )
        self.fill_rent_form(
            order_data["date"],
            order_data["period"],
            order_data["color"],
            order_data["comment"],
        )
        self.submit_order()
