import allure
from pages.order_tape_page import OrderTapePage
from pages.main_page import MainPage
from pages.private_office_page import PrivateOfficePage
from constants import Constants


class TestOrderTape:

    @allure.title('Проверка появления всплывающего окна с деталями заказа')
    def test_appearance_order_window(self, driver):
        order = OrderTapePage(driver)
        order.go_to_site(Constants.URL_ORDER_PAGE)
        order.loading_order_page()
        order.click_on_order()
        order.wait_for_order_window()
        order_composition = order.get_order_composition()

        assert order_composition.text == 'Cостав'

    @allure.title('Проверка отображения заказов пользователя из истории заказов в ленте заказов')
    @allure.description('1.Залогиниться под пользователем.'
                        '2.Создать заказ.'
                        '3.Получить номер заказа из раздела «История заказов».'
                        '4.Проверить, что данный номер заказа отображается в разделе «Лента заказов».')
    def test_client_can_find_order_in_history_and_in_tape(self, prepare_user, driver):
        user = PrivateOfficePage(driver)
        user.go_to_site(Constants.URL_LOGIN)
        email = "Ilya92@yandex.ru"
        password = "Il1992"
        user.login_to_private_account(email, password)
        main = MainPage(driver)
        main.create_order(driver)
        main.click_on_close_cross()
        main.click_on_private_office_button()
        user.loading_profile_page()
        user.go_to_history_order()
        order = OrderTapePage(driver)
        order_number_history = order.get_order_number()
        main.go_to_order_tape()
        order_number_tape = order.get_order_number()

        assert order_number_history == order_number_tape

    @allure.title('Проверка увеличения значения общего счетчика заказов при создании нового заказа')
    @allure.description('1.Залогиниться под пользователем.'
                        '2.Получить значение общего счетчика заказов ДО создания заказа.'
                        '3.Создать заказ.'
                        '4.Получить значение общего счетчика заказов ПОСЛЕ создания заказа.'
                        '5.Проверить, что значение общего счетчика заказов увеличилось на 1')
    def test_increase_counter_for_all_orders(self, prepare_user, driver):
        user = PrivateOfficePage(driver)
        user.go_to_site(Constants.URL_LOGIN)
        email = "Ilya92@yandex.ru"
        password = "Il1992"
        user.login_to_private_account(email, password)
        main = MainPage(driver)
        main.loading_main_page()
        main.click_on_orders_tape()
        main.loading_order_page()
        order = OrderTapePage(driver)
        counter_orders_before = order.get_counter_for_all_orders()
        main.click_on_constructor_logo()
        main.create_order(driver)
        main.click_on_close_cross()
        main.go_to_order_tape()
        counter_order_after = order.get_counter_for_all_orders()

        assert int(counter_order_after) == int(counter_orders_before) + 1

    @allure.title('Проверка увеличения значения счетчика заказов за сегодня при создании нового заказа')
    @allure.description('1.Залогиниться под пользователем.'
                        '2.Получить значение счетчика заказов за сегодня ДО создания заказа.'
                        '3.Создать заказ.'
                        '4.Получить значение счетчика заказов за чегодня ПОСЛЕ создания заказа.'
                        '5.Проверить, что значение счетчика заказов за сегодня увеличилось на 1')
    def test_increase_counter_for_today_orders(self, prepare_user, driver):
        user = PrivateOfficePage(driver)
        user.go_to_site(Constants.URL_LOGIN)
        email = "Ilya92@yandex.ru"
        password = "Il1992"
        user.login_to_private_account(email, password)
        main = MainPage(driver)
        main.loading_main_page()
        main.click_on_orders_tape()
        main.loading_order_page()
        order = OrderTapePage(driver)
        counter_today_before = order.get_counter_for_today_orders()
        main.click_on_constructor_logo()
        main.create_order(driver)
        main.click_on_close_cross()
        main.go_to_order_tape()
        counter_today_after = order.get_counter_for_today_orders()

        assert int(counter_today_after) == int(counter_today_before) + 1

    @allure.title('Проверка, что новый заказ отображается в разделе «В работе»')
    @allure.description('1.Залогиниться под пользователем.'
                        '2.Создать заказ.'
                        '3.Получаем номер заказа.'
                        '4.Проверяем, что номер заказа появился в разделе «В работе».')
    def test_get_number_from_section_in_progress(self, prepare_user, driver):
        user = PrivateOfficePage(driver)
        user.go_to_site(Constants.URL_LOGIN)
        email = "Ilya92@yandex.ru"
        password = "Il1992"
        user.login_to_private_account(email, password)
        main = MainPage(driver)
        main.create_order(driver)
        order = OrderTapePage(driver)
        number_from_pop_up = order.get_number_from_pop_up_window()
        main.click_on_close_cross()
        main.go_to_order_tape()
        number_in_progress = order.get_number_from_section_in_progress()

        assert number_from_pop_up == number_in_progress

