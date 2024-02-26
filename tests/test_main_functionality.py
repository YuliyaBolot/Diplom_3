import allure
from selenium.webdriver import ActionChains
from pages.private_office_page import PrivateOfficePage
from pages.main_page import MainPage
from constants import Constants


class TestMainFunctionality:

    @allure.title('Проверка перехода по клику на «Конструктор»')
    def test_click_on_constructor(self, driver):
        private = PrivateOfficePage(driver)
        private.go_to_site(Constants.URL_LOGIN)
        private.loading_login_page()
        main = MainPage(driver)
        main.click_on_constructor_logo()
        main.loading_main_page()

        assert Constants.URL == driver.current_url

    @allure.title('Проверка перехода по клику на «Лента заказов»')
    def test_click_on_orders_tape(self, driver):
        main = MainPage(driver)
        main.go_to_site(Constants.URL)
        main.loading_main_page()
        main.click_on_orders_tape()
        main.loading_order_page()

        assert Constants.URL_ORDER_PAGE == driver.current_url

    @allure.title('Проверка появления высплывающего окна с деталями ингредиента')
    def test_click_on_ingredient(self, driver):
        main = MainPage(driver)
        main.go_to_site(Constants.URL)
        main.loading_main_page()
        main.wait_for_ingredient_lst()
        main.click_on_ingredient()
        main.wait_for_pop_up_window_ingredient()

        assert Constants.URL_INGREDIENTS in driver.current_url

    @allure.title('Проверка закрытия высплывающего окна с деталями ингредиента')
    def test_close_pop_up_window_ingredient(self, driver):
        main = MainPage(driver)
        main.go_to_site(Constants.URL)
        main.loading_main_page()
        main.wait_for_ingredient_lst()
        main.click_on_ingredient()
        main.wait_for_pop_up_window_ingredient()
        main.click_on_close_cross()

        assert main.wait_close_ingredient_details()

    @allure.title('Увеличение счетчика ингредиента при добавлении его в заказ')
    def test_ingredient_count(self, driver):
        main = MainPage(driver)
        main.go_to_site(Constants.URL)
        main.loading_main_page()
        ingredient = main.find_ingredient()
        add_to_order = main.add_to_order()
        ActionChains(driver).drag_and_drop(ingredient, add_to_order).perform()
        main.wait_appearance_ingredient_in_order()
        count = main.get_count_number()

        assert int(count) == 1

    @allure.title('Проверка возможности оформления заказа залогиненным пользователем')
    def test_create_order_by_login_user(self, driver, prepare_user):
        user = PrivateOfficePage(driver)
        user.go_to_site(Constants.URL_LOGIN)
        email = "Ilya92@yandex.ru"
        password = "Il1992"
        user.login_to_private_account(email, password)
        main = MainPage(driver)
        main.loading_main_page()
        ingredient_bun = main.find_ingredient_bun()
        add_to_order_bun = main.add_to_order()
        ActionChains(driver).drag_and_drop(ingredient_bun, add_to_order_bun).perform()
        order_button = main.wait_create_order_button()

        assert order_button.text == 'Оформить заказ'

