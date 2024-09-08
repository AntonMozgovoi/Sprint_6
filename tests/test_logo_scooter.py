import allure
from data import Urls
from pages.main_page import MainPage


class TestLogoScooter:
    @allure.title('Проверка перехода при клике по логотипу')
    @allure.description('Проверяем переход к главной странице при клике по логотипу "Самокат"')
    def test_transition_on_main(self, driver):
        logo_scooter = MainPage(driver)
        logo_scooter.find_and_click_scooter()
        assert driver.current_url == Urls.MAIN_PAGE