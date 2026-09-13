from selenium.webdriver.common.by import By


class MainPageLocators:
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
    def question(index):
        return By.ID, f"accordion__heading-{index}"

    @staticmethod
    def answer(index):
        return By.ID, f"accordion__panel-{index}"
