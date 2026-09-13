import allure
import pytest

from data import FaqData
from pages.main_page import MainPage


@allure.feature("Вопросы о важном")
class TestFaq:

    @allure.title("Проверка ответа на вопрос №{index}")
    @pytest.mark.parametrize(
        "index, expected_answer",
        FaqData.QUESTIONS_AND_ANSWERS,
    )
    def test_question_opens_correct_answer(
        self,
        driver,
        index,
        expected_answer,
    ):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.close_cookie_banner()

        main_page.open_question(index)
        actual_answer = main_page.get_answer(index)

        assert actual_answer == expected_answer
