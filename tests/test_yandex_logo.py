import time
from selenium.webdriver.support.wait import WebDriverWait
import allure
from data import Urls
from pages.main_page import MainPage


class TestLogoYandex:
    @allure.title('Проверка перехода при клике по логотипу')
    @allure.description('Проверяем открытие странице "Яндекс Дзен" при клике по логотипу "Яндекс"')
    def test_transition_on_dzen(self, driver):
        logo_yandex = MainPage(driver)
        logo_yandex.find_and_click_yandex()
        new_tab = driver.window_handles[1]
        driver.switch_to.window(new_tab)
        logo_yandex.find_dzen()
        assert driver.current_url == Urls.DZEN_PAGE