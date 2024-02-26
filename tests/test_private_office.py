import allure
from pages.private_office_page import PrivateOfficePage
from pages.main_page import MainPage
from constants import Constants


class TestPrivateOffice:

    @allure.title('Проверка перехода по клику на «Личный кабинет»')
    def test_go_to_private_office(self, prepare_user, driver):
        user = PrivateOfficePage(driver)
        user.go_to_site(Constants.URL_LOGIN)
        email = "Ilya92@yandex.ru"
        password = "Il1992"
        user.login_to_private_account(email, password)
        main = MainPage(driver)
        main.loading_main_page()
        main.click_on_private_office_button()
        user.loading_profile_page()

        assert Constants.URL_PROFILE == driver.current_url

    @allure.title('Проверка перехода в раздел «История заказов»')
    def test_go_to_history_order(self, prepare_user, driver):
        user = PrivateOfficePage(driver)
        user.go_to_site(Constants.URL_LOGIN)
        email = "Ilya92@yandex.ru"
        password = "Il1992"
        user.login_to_private_account(email, password)
        main = MainPage(driver)
        main.loading_main_page()
        main.click_on_private_office_button()
        user.loading_profile_page()
        user.go_to_history_order()

        assert Constants.URL_HISTORY_ORDER == driver.current_url

    @allure.title('Проверка выхода из аккаунта')
    def test_exit_from_private_account(self, prepare_user, driver):
        user = PrivateOfficePage(driver)
        user.go_to_site(Constants.URL_LOGIN)
        email = "Ilya92@yandex.ru"
        password = "Il1992"
        user.login_to_private_account(email, password)
        main = MainPage(driver)
        main.loading_main_page()
        main.click_on_private_office_button()
        user.loading_profile_page()
        user.click_on_exit_button()
        user.loading_login_page()

        assert Constants.URL_LOGIN == driver.current_url

