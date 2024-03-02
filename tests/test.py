import allure
from pages.main_page import MainPage
from constants import Urls


class Test:

    @allure.title('Увеличение счетчика ингредиента при добавлении его в заказ')
    def test_ingredient_count(self, driver):
        main = MainPage(driver)
        main.go_to_site(Urls.URL)
        main.loading_main_page()
        ingredient = main.find_ingredient()
        add_to_order = main.add_to_order()
        main.drag_and_drop(ingredient, add_to_order).perform()
        main.wait_appearance_ingredient_in_order()
        count = main.get_count_number()

        assert int(count) == 1

    @allure.title('Проверка перехода по клику на «Лента заказов»')
    def test_click_on_orders_tape(self, driver):
        main = MainPage(driver)
        main.go_to_site(Urls.URL)
        main.loading_main_page()
        main.click_on_orders_tape()
        main.loading_order_page()

        assert Urls.URL_ORDER_PAGE == main.current_url

