from pages.base_page import BasePage
from locators.main_locators import MainLocators
from selenium.webdriver import ActionChains


class MainPage(BasePage):

    def loading_main_page(self):
        return self.find_element_located(MainLocators.MAIN_PAGE)

    def click_on_private_office_button(self):
        return self.find_element_located_click(MainLocators.PRIVATE_OFFICE_BUTTON)

    def click_on_constructor_logo(self):
        return self.find_element_located_click(MainLocators.CONSTRUCTOR_BUTTON)

    def click_on_orders_tape(self):
        return self.find_element_located_click(MainLocators.ORDERS_TAPE)

    def loading_order_page(self):
        return self.find_element_located(MainLocators.ORDER_PAGE)

    def wait_for_ingredient_lst(self):
        return self.find_element_located(MainLocators.INGREDIENT_LST)

    def click_on_ingredient(self):
        return self.find_element_located_click(MainLocators.INGREDIENT)

    def wait_for_pop_up_window_ingredient(self):
        return self.find_element_located(MainLocators.POP_UP_WINDOW)

    def click_on_close_cross(self):
        return self.find_element_located_click(MainLocators.CLOSE_POP_UP_WINDOW)

    def wait_close_ingredient_details(self):
        return self.find_element_located(MainLocators.CLOSE_INGREDIENT_DETAILS)

    def find_ingredient(self):
        return self.find_element_located(MainLocators.INGREDIENT)

    def find_ingredient_bun(self):
        return self.find_element_located(MainLocators.INGREDIENT_BUN)

    def add_to_order(self):
        return self.find_element_located(MainLocators.ORDER_BASKET)

    def wait_appearance_ingredient_in_order(self):
        return self.find_element_located(MainLocators.PLACE_FOR_INGREDIENT)

    def get_count_number(self):
        return self.find_element_located(MainLocators.COUNT_INGREDIENT).text

    def wait_create_order_button(self):
        return self.find_element_located(MainLocators.CREATE_ORDER_BUTTON)

    def click_on_create_order_button(self):
        return self.find_element_located_click(MainLocators.CREATE_ORDER_BUTTON)

    def wait_for_order_pop_up_window(self):
        return self.find_element_located(MainLocators.POP_UP_WINDOW, time=30)

    def create_order(self, driver):
        self.loading_main_page()
        ingredient_filling = self.find_ingredient()
        add_to_order = self.add_to_order()
        ActionChains(driver).drag_and_drop(ingredient_filling, add_to_order).perform()
        ingredient_bun = self.find_ingredient_bun()
        add_to_order_bun = self.add_to_order()
        ActionChains(driver).drag_and_drop(ingredient_bun, add_to_order_bun).perform()
        self.click_on_create_order_button()
        self.wait_for_order_pop_up_window()

    def go_to_order_tape(self):
        self.click_on_orders_tape()
        self.loading_order_page()
