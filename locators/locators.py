from selenium.webdriver.common.by import By


class MainPageLocators:
    JUST_KILL_COOKIE = (By.XPATH, '//button[starts-with(@class, "App_CookieButton")]')
    SCOOTER_LOGO = (By.XPATH, '//*[contains(@Class, "Header_LogoScooter")]')
    YANDEX_LOGO = (By.XPATH, '//*[contains(@Class, "Header_LogoYandex")]')
    @staticmethod                       # функция получения локатора кнопки "Заказать"
    def get_question_answer(button_class):
        return By.XPATH, f'//button[@class = "{button_class}"]'


class FirstFormFields:
    NAME_FIELD = (By.XPATH, '//input[@placeholder="* Имя"]')
    SECOND_NAME_FIELD = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS_FIELD = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_STATION_FIELD = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    NAME_STATION = (By.XPATH, '//div[text()="Полежаевская"]')
    TELEPHONE_FIELD = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.XPATH, '//button[text()="Далее"]')


class SecondFormFields:
    WHEN_DELIVERY = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    DATE_OF_DELIVERY = (By.XPATH, '//div[@aria-label="Choose суббота, 31-е августа 2024 г."]')
    RENT_TERN_FIELD = (By.XPATH, '//div[text()="* Срок аренды"]')
    RENT_TERN_SELECTED = (By.XPATH, '//div[text()="сутки"]')
    SELECT_COLOR = (By.XPATH, '//*[@id="grey"]')
    COMMENTS = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    SECOND_BUTTON_ORDER = (By.XPATH, '//button[contains(@Class, "Button_Middle_") and text()="Заказать"]')
    BUTTON_CONFIRM = (By.XPATH, '//button[contains(@Class, "Button_Button") and text()="Да"]')

    WINDOW_SUCCESS_ORDER = (By.XPATH, '//div[starts-with(@class, "Order_Modal") and text()="Заказ оформлен"]')


class AnswearQuestion:

    @staticmethod  # функция получения локатора для вопроса
    def get_question(number):
        return By.XPATH, f'//*[@id="accordion__heading-{number}"]'

    @staticmethod  # функция получения локатора для ответа
    def get_answer(number):
        return By.XPATH, f'//*[@id="accordion__panel-{number}"]'
