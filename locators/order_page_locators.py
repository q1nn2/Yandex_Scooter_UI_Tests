from selenium.webdriver.common.by import By


class OrderPageLocators:
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
