from locators.locators import SecondFormFields
from pages.base_page import BasePage


class OrderPage(BasePage):

    def date_of_delivery(self):
        when = self.wait_and_find_element(SecondFormFields.WHEN_DELIVERY)
        when.click()

    def select_date(self):
        date_delivery = self.wait_and_find_element(SecondFormFields.DATE_OF_DELIVERY)
        date_delivery.click()

    def select_rent_term(self):
        rent_term = self.wait_and_find_element(SecondFormFields.RENT_TERN_FIELD)
        rent_term.click()

    def select_day(self):
        select_day = self.wait_and_find_element(SecondFormFields.RENT_TERN_SELECTED)
        select_day.click()

    def select_color(self):
        select_color = self.wait_and_find_element(SecondFormFields.SELECT_COLOR)
        select_color.click()

    def input_comments(self, value):
        comments = self.wait_and_find_element(SecondFormFields.COMMENTS)
        comments.send_keys(value)

    def click_final_button(self):
        second_order_button = self.wait_and_find_element(SecondFormFields.SECOND_BUTTON_ORDER)
        second_order_button.click()

    def click_confirmation(self):
        confirmation = self.wait_and_find_element(SecondFormFields.BUTTON_CONFIRM)
        confirmation.click()

    def order_window(self):
        success = self.wait_and_find_element(SecondFormFields.WINDOW_SUCCESS_ORDER)
        return success
