import allure
from pages.base_page import BasePage
from locators.main_locators import MainLocators


class MainPage(BasePage):

    @allure.step("Загрузка главной страницы приложения Stellar Burgers")
    def loading_main_page(self):
        return self.find_element_located(MainLocators.MAIN_PAGE)

    @allure.step("Нажимаем на кнопку 'Личный Кабинет'")
    def click_on_private_office_button(self):
        return self.find_element_located_click(MainLocators.PRIVATE_OFFICE_BUTTON)

    @allure.step("Нажимаем на логотип 'Конструктор'")
    def click_on_constructor_logo(self):
        return self.find_element_located_click(MainLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Нажимаем на кнопку 'Лента Заказов'")
    def click_on_orders_tape(self):
        return self.find_element_located_click(MainLocators.ORDERS_TAPE)

    @allure.step("Загрузка страницы 'Лента Заказов'")
    def loading_order_page(self):
        return self.find_element_located(MainLocators.ORDER_PAGE)

    @allure.step("Ожидаем загрузки списка ингредиентов")
    def wait_for_ingredient_lst(self):
        return self.find_element_located(MainLocators.INGREDIENT_LST)

    @allure.step("Нажимаем на ингредиент")
    def click_on_ingredient(self):
        return self.find_element_located_click(MainLocators.INGREDIENT)

    @allure.step("Ожидаем пояления всплывающего окна с деталями ингредиента")
    def wait_for_pop_up_window_ingredient(self):
        return self.find_element_located(MainLocators.POP_UP_WINDOW)

    @allure.step("Закрываем всплывающее окно с деталями ингредиента")
    def click_on_close_cross(self):
        return self.find_element_located_click(MainLocators.CLOSE_POP_UP_WINDOW)

    @allure.step("Всплывающее окно с деталями ингредиента закрыто")
    def wait_close_ingredient_details(self):
        return self.find_element_located(MainLocators.CLOSE_INGREDIENT_DETAILS)

    @allure.step("Добавляем ингредиент в заказ")
    def drag_and_drop_ingredient(self):
        return self.drag_and_drop(MainLocators.INGREDIENT, MainLocators.ORDER_BASKET)

    @allure.step("Добавляем булку в заказ")
    def drag_and_drop_bun(self):
        return self.drag_and_drop(MainLocators.INGREDIENT_BUN, MainLocators.ORDER_BASKET)

    @allure.step("Ожидаем появления ингредиента в заказе")
    def wait_appearance_ingredient_in_order(self):
        return self.find_element_located(MainLocators.PLACE_FOR_INGREDIENT)

    @allure.step("Получаем счетчик ингредиента")
    def get_count_number(self):
        return self.find_element_located(MainLocators.COUNT_INGREDIENT).text

    @allure.step("Ожидаем появления кнопки оформления заказа")
    def wait_create_order_button(self):
        return self.find_element_located(MainLocators.CREATE_ORDER_BUTTON)

    @allure.step("Нажимаем на кнопку оформления заказа")
    def click_on_create_order_button(self):
        return self.find_element_located_click(MainLocators.CREATE_ORDER_BUTTON)

    @allure.step("Ожидаем пояления всплывающего окна с номером заказа")
    def wait_for_order_pop_up_window(self):
        return self.find_element_located(MainLocators.POP_UP_WINDOW, time=30)

    @allure.step("Создаем заказ")
    def create_order(self):
        self.loading_main_page()
        self.drag_and_drop_ingredient()
        self.drag_and_drop_bun()
        self.click_on_create_order_button()
        self.wait_for_order_pop_up_window()

    @allure.step("Переходим на страницу 'Лента заказов'")
    def go_to_order_tape(self):
        self.click_on_orders_tape()
        self.loading_order_page()
