import allure
from pages.base_page import BasePage
from locators.order_tape_locators import OrderTapeLocators


class OrderTapePage(BasePage):

    @allure.step("Загрузка страницы 'Лента заказов'")
    def loading_order_page(self):
        return self.find_element_located(OrderTapeLocators.ORDER_PAGE)

    @allure.step("Нажимаем на заказ")
    def click_on_order(self):
        return self.find_element_located_click(OrderTapeLocators.ORDER)

    @allure.step("Ожидаем появление всплывающего окна с деталями заказа")
    def wait_for_order_window(self):
        return self.find_element_located(OrderTapeLocators.ORDER_WINDOW)

    @allure.step("Получаем состав заказа")
    def get_order_composition(self):
        return self.find_element_located(OrderTapeLocators.ORDER_COMPOSITION)

    @allure.step("Получаем номер заказа")
    def get_order_number(self):
        return self.find_element_located(OrderTapeLocators.ORDER_NUMBER).text

    @allure.step("Получаем счетчик всех заказов, выполенных за все время")
    def get_counter_for_all_orders(self):
        return self.find_element_located(OrderTapeLocators.COUNTER_ALL_ORDERS).text

    @allure.step("Получаем счетчик всех заказов, выполенных за сегодня")
    def get_counter_for_today_orders(self):
        return self.find_element_located(OrderTapeLocators.COUNTER_TODAY_ORDERS).text

    @allure.step("Получаем номер заказа из всплывающего окна оформления заказа")
    def get_number_from_pop_up_window(self):
        return self.find_element_located(OrderTapeLocators.NUMBER_FROM_POP_UP, time=15).text

    @allure.step("Получаем номер заказа из раздела 'В работе'")
    def get_number_from_section_in_progress(self):
        return self.find_element_located(OrderTapeLocators.NUMBER_IN_PROGRESS, time=5).text







