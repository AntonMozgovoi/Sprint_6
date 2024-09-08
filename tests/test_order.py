import allure
import pytest
import data
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrder:
    @allure.title('Проверка успешного заказа')
    @allure.description('Проверяем весь флоу позитивного сценария с применением параметризации и двух наборов данных')
    @pytest.mark.parametrize(data.FirstFormData.parameter, data.FirstFormData.value)
    def test_order_success(self, driver, BUTTON_CLASS, NAME, SURNAME, ADDRESS, PHONE, COMMENTS):
        order = MainPage(driver)
        order.kill_cookie()
        order.click_buttons(BUTTON_CLASS)
        order.name_input(NAME)
        order.surname_input(SURNAME)
        order.address_input(ADDRESS)
        order.select_station()
        order.name_station()
        order.phone_input(PHONE)
        order.click_next_button()

        order = OrderPage(driver)
        order.date_of_delivery()
        order.select_date()
        order.select_rent_term()
        order.select_day()
        order.select_color()
        order.input_comments(COMMENTS)
        order.click_final_button()
        order.click_confirmation()
        order_success = order.order_window()
        assert order_success.is_displayed()
