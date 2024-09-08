from locators.locators import MainPageLocators, FirstFormFields, AnswearQuestion
from pages.base_page import BasePage


class MainPage(BasePage):

    def kill_cookie(self):  # согласие с куками
        button = self.wait_and_find_element(MainPageLocators.JUST_KILL_COOKIE)
        button.click()

    def name_input(self, name):  # ввод имени
        name_field = self.wait_and_find_element(FirstFormFields.NAME_FIELD)
        name_field.send_keys(name)

    def surname_input(self, name):  # ввод фамилии
        second_name_field = self.wait_and_find_element(FirstFormFields.SECOND_NAME_FIELD)
        second_name_field.send_keys(name)

    def address_input(self, address):  # ввод адреса
        address_field = self.wait_and_find_element(FirstFormFields.ADDRESS_FIELD)
        address_field.send_keys(address)

    def select_station(self):  # клик по полю списка станций метро
        station = self.wait_and_find_element(FirstFormFields.METRO_STATION_FIELD)
        station.click()

    def name_station(self):
        name_station = self.wait_and_find_element(FirstFormFields.NAME_STATION)
        name_station.click()

    def phone_input(self, number):
        phone = self.wait_and_find_element(FirstFormFields.TELEPHONE_FIELD)
        phone.send_keys(number)

    def click_next_button(self):
        next_button = self.wait_and_find_element(FirstFormFields.NEXT_BUTTON)
        next_button.click()

    def click_buttons(self, button_class):
        buuttons = self.wait_and_find_element(MainPageLocators.get_question_answer(button_class))
        buuttons.click()

    def find_question(self, number):  # поиск и клик по вопросу
        question = self.wait_and_find_element(AnswearQuestion.get_question(number))
        question.click()

    def find_answer(self, number):
        answer = self.wait_and_find_element(AnswearQuestion.get_answer(number))  # поиск и получение текса ответа
        return answer.text

    def find_and_click_scooter(self):  # поиск и клик кнопки "Самокат"
        scooter = self.wait_and_find_element(MainPageLocators.SCOOTER_LOGO)
        scooter.click()

    def find_and_click_yandex(self):
        logo_yandex = self.wait_and_find_element(MainPageLocators.YANDEX_LOGO)
        logo_yandex.click()

    def find_dzen(self):
        dzen = self.wait_and_find_element(MainPageLocators.DZEN)