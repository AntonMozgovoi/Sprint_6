import allure
import pytest
import data
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrder:
    @allure.title('Проверка успешного заказа')
    @allure.description('Проверяем весь флоу позитивного сценария с применением параметризации и двух наборов данных')
    @pytest.mark.parametrize(data.FirstFormData.parameter, data.FirstFormData.value)
    def test_order_success(self, driver, button_class, name, surname, address, phone, comments,):
        order = MainPage(driver)
        order.kill_cookie()
        order.click_buttons(button_class)
        order.name_input(name)
        order.surname_input(surname)
        order.address_input(address)
        order.select_station()
        order.name_station()
        order.phone_input(phone)
        order.click_next_button()

        order = OrderPage(driver)
        order.date_of_delivery()
        order.select_date()
        order.select_rent_term()
        order.select_day()
        order.select_color()
        order.input_comments(comments)
        order.click_final_button()
        order.click_confirmation()
        order_success = order.order_window()
        assert order_success.is_displayed()
