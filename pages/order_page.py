import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class OrderPage(BasePage):
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Адрес: куда привезти заказ']"
    )
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Телефон: на него позвонит курьер']"
    )
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    DELIVERY_DATE_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Когда привезти самокат']"
    )
    RENT_PERIOD_DROPDOWN = (
        By.XPATH,
        "//div[contains(@class,'Dropdown-placeholder')]"
    )
    BLACK_COLOR = (By.ID, "black")
    GREY_COLOR = (By.ID, "grey")
    COMMENT_INPUT = (
        By.XPATH,
        "//input[@placeholder='Комментарий для курьера']"
    )
    ORDER_BUTTON = (
        By.XPATH,
        "//div[contains(@class,'Order_Buttons')]//button[text()='Заказать']"
    )

    CONFIRM_BUTTON = (
        By.XPATH,
        "//div[contains(@class,'Order_Modal')]//button[text()='Да']"
    )
    SUCCESS_TITLE = (
        By.XPATH,
        "//*[contains(@class,'Order_ModalHeader') and contains(text(),'Заказ оформлен')]"
    )

    @staticmethod
    def metro_option(station):
        return (
            By.XPATH,
            "//div[contains(@class,'select-search__select')]"
            f"//*[normalize-space()='{station}']"
        )

    @staticmethod
    def rent_period_option(period):
        return (
            By.XPATH,
            "//div[contains(@class,'Dropdown-option') and "
            f"normalize-space()='{period}']"
        )

    @allure.step("Заполнить форму «Для кого самокат»")
    def fill_customer_form(self, name, surname, address, metro, phone):
        self.type_text(self.NAME_INPUT, name)
        self.type_text(self.SURNAME_INPUT, surname)
        self.type_text(self.ADDRESS_INPUT, address)

        metro_input = self.find(self.METRO_INPUT)
        metro_input.click()
        metro_input.send_keys(metro)
        self.click(self.metro_option(metro))

        self.type_text(self.PHONE_INPUT, phone)
        self.click(self.NEXT_BUTTON)

        self.wait.until(
            EC.visibility_of_element_located(self.DELIVERY_DATE_INPUT)
        )

    @allure.step("Указать дату доставки: {date}")
    def set_delivery_date(self, date):
        date_input = self.find(self.DELIVERY_DATE_INPUT)
        date_input.clear()
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)

    @allure.step("Выбрать срок аренды: {period}")
    def select_rent_period(self, period):
        self.click(self.RENT_PERIOD_DROPDOWN)
        self.click(self.rent_period_option(period))

    @allure.step("Выбрать цвет самоката: {color}")
    def select_color(self, color):
        if color == "black":
            self.click(self.BLACK_COLOR)
        elif color == "grey":
            self.click(self.GREY_COLOR)
        else:
            raise ValueError(f"Неизвестный цвет: {color}")

    @allure.step("Ввести комментарий для курьера")
    def set_comment(self, comment):
        self.type_text(self.COMMENT_INPUT, comment)

    @allure.step("Заполнить форму «Про аренду»")
    def fill_rent_form(self, date, period, color, comment):
        self.set_delivery_date(date)
        self.select_rent_period(period)
        self.select_color(color)
        self.set_comment(comment)

    @allure.step("Подтвердить заказ")
    def submit_order(self):
        self.scroll_to(self.ORDER_BUTTON)
        self.click(self.ORDER_BUTTON)
        self.click(self.CONFIRM_BUTTON)

    @allure.step("Проверить сообщение об успешном оформлении заказа")
    def get_success_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_TITLE)
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
