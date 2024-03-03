import allure
from pages.private_office_page import PrivateOfficePage
from pages.main_page import MainPage
from constants import Urls


class TestPrivateOffice:

    @allure.title('Проверка перехода по клику на «Личный кабинет»')
    def test_go_to_private_office(self, prepare_user, login_user, driver):
        main = MainPage(driver)
        main.loading_main_page()
        main.click_on_private_office_button()
        user = PrivateOfficePage(driver)
        user.loading_profile_page()
        current_url = user.current_url()

        assert Urls.URL_PROFILE == current_url

    @allure.title('Проверка перехода в раздел «История заказов»')
    def test_go_to_history_order(self, prepare_user, login_user, driver):
        main = MainPage(driver)
        main.loading_main_page()
        main.click_on_private_office_button()
        user = PrivateOfficePage(driver)
        user.loading_profile_page()
        user.go_to_history_order()
        current_url = user.current_url()

        assert Urls.URL_HISTORY_ORDER == current_url

    @allure.title('Проверка выхода из аккаунта')
    def test_exit_from_private_account(self, prepare_user, login_user, driver):
        main = MainPage(driver)
        main.loading_main_page()
        main.click_on_private_office_button()
        user = PrivateOfficePage(driver)
        user.loading_profile_page()
        user.click_on_exit_button()
        user.loading_login_page()
        current_url = user.current_url()

        assert Urls.URL_LOGIN == current_url


