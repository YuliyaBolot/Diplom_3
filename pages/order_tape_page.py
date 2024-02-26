from pages.base_page import BasePage
from locators.order_tape_locators import OrderTapeLocators


class OrderTapePage(BasePage):

    def loading_order_page(self):
        return self.find_element_located(OrderTapeLocators.ORDER_PAGE)

    def click_on_order(self):
        return self.find_element_located_click(OrderTapeLocators.ORDER)

    def wait_for_order_window(self):
        return self.find_element_located(OrderTapeLocators.ORDER_WINDOW)

    def get_order_composition(self):
        return self.find_element_located(OrderTapeLocators.ORDER_COMPOSITION)

    def get_order_number(self):
        return self.find_element_located(OrderTapeLocators.ORDER_NUMBER).text

    def get_counter_for_all_orders(self):
        return self.find_element_located(OrderTapeLocators.COUNTER_ALL_ORDERS).text

    def get_counter_for_today_orders(self):
        return self.find_element_located(OrderTapeLocators.COUNTER_TODAY_ORDERS).text

    def get_number_from_pop_up_window(self):
        return self.find_element_located(OrderTapeLocators.NUMBER_FROM_POP_UP, time=15).text

    def get_number_from_section_in_progress(self):
        return self.find_element_located(OrderTapeLocators.NUMBER_IN_PROGRESS, time=5).text







