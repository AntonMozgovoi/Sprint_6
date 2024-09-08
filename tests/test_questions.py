import allure

import data
from pages.main_page import MainPage
import pytest


class TestQuestionForm:
    @allure.title('Проверка списка с вопросами')
    @allure.description('Проверяем соответствие теста ответов на вопросы')
    @pytest.mark.parametrize(data.GetAnswear.parameter, data.GetAnswear.value)
    def test_first_questions(self, driver, NUMBER, EXPECTED_ANSWER):
        question_form = MainPage(driver)
        question_form.kill_cookie()
        question_form.find_question(NUMBER)
        question_form.find_answer(NUMBER)
        assert question_form.find_answer(NUMBER) == EXPECTED_ANSWER
