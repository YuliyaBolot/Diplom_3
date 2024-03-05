import allure
from pages.private_office_page import PrivateOfficePage
from pages.main_page import MainPage
from constants import Urls


class TestMainFunctionality:

    @allure.title('Проверка перехода по клику на «Конструктор»')
    def test_click_on_constructor(self, driver):
        private = PrivateOfficePage(driver)
        private.go_to_site(Urls.URL_LOGIN)
        private.loading_login_page()
        main = MainPage(driver)
        main.click_on_constructor_logo()
        main.loading_main_page()
        current_url = main.current_url()

        assert Urls.URL == current_url

    @allure.title('Проверка перехода по клику на «Лента заказов»')
    def test_click_on_orders_tape(self, driver):
        main = MainPage(driver)
        main.go_to_site(Urls.URL)
        main.loading_main_page()
        main.click_on_orders_tape()
        main.loading_order_page()
        current_url = main.current_url()

        assert Urls.URL_ORDER_PAGE == current_url

    @allure.title('Проверка появления высплывающего окна с деталями ингредиента')
    def test_click_on_ingredient(self, driver):
        main = MainPage(driver)
        main.go_to_site(Urls.URL)
        main.loading_main_page()
        main.wait_for_ingredient_lst()
        main.click_on_ingredient()
        main.wait_for_pop_up_window_ingredient()
        current_url = main.current_url()

        assert Urls.URL_INGREDIENTS in current_url

    @allure.title('Проверка закрытия высплывающего окна с деталями ингредиента')
    def test_close_pop_up_window_ingredient(self, driver):
        main = MainPage(driver)
        main.go_to_site(Urls.URL)
        main.loading_main_page()
        main.wait_for_ingredient_lst()
        main.click_on_ingredient()
        main.wait_for_pop_up_window_ingredient()
        main.click_on_close_cross()

        assert main.wait_close_ingredient_details()

    @allure.title('Увеличение счетчика ингредиента при добавлении его в заказ')
    def test_ingredient_count(self, driver):
        main = MainPage(driver)
        main.go_to_site(Urls.URL)
        main.loading_main_page()
        main.drag_and_drop_ingredient()
        main.wait_appearance_ingredient_in_order()
        count = main.get_count_number()

        assert int(count) == 1

    @allure.title('Проверка возможности оформления заказа залогиненным пользователем')
    def test_create_order_by_login_user(self, driver, prepare_user, login_user):
        main = MainPage(driver)
        main.go_to_site(Urls.URL)
        main.loading_main_page()
        main.drag_and_drop_bun()
        order_button = main.wait_create_order_button()

        assert order_button.text == 'Оформить заказ'

