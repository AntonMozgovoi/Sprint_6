import allure

import data
from pages.main_page import MainPage
import pytest


class TestQuestionForm:
    @allure.title('Проверка списка с вопросами')
    @allure.description('Проверяем соответствие теста ответов на вопросы')
    @pytest.mark.parametrize(data.GetAnswear.parameter, data.GetAnswear.value)
    def test_first_questions(self, driver, number, expected_answer):
        question_form = MainPage(driver)
        question_form.kill_cookie()
        question_form.find_question(number)
        question_form.find_answer(number)
        assert question_form.find_answer(number) == expected_answer
