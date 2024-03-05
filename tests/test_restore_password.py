import allure
from pages.private_office_page import PrivateOfficePage
from pages.restore_password_page import RestorePasswordPage
from constants import Urls
from faker import Faker

faker = Faker()


class TestRestorePassword:

    @allure.title('Проверка перехода на страницу восстановления пароля по ссылке «Восстановить пароль»')
    def test_move_to_restore_password_page(self, driver):
        login = PrivateOfficePage(driver)
        login.go_to_site(Urls.URL_LOGIN)
        login.loading_login_page()
        restore = RestorePasswordPage(driver)
        restore.click_on_restore_password_link()
        restore.loading_forgot_password_page()
        current_url = restore.current_url()

        assert Urls.URL_FORGOT_PASSWORD == current_url

    @allure.title('Проверка перехода на страницу сброса пароля при вводе email')
    def test_input_email(self, driver):
        restore = RestorePasswordPage(driver)
        restore.go_to_site(Urls.URL_FORGOT_PASSWORD)
        restore.loading_forgot_password_page()
        email = faker.email()
        restore.set_email(email)
        restore.click_on_restore_button()
        restore.loading_field_for_code()
        current_url = restore.current_url()

        assert Urls.URL_RESET_PASSWORD == current_url

    @allure.title('Проверка активации поля для ввода пароля')
    def test_active_password_field(self, driver):
        restore = RestorePasswordPage(driver)
        restore.go_to_site(Urls.URL_FORGOT_PASSWORD)
        restore.loading_forgot_password_page()
        email = faker.email()
        restore.set_email(email)
        restore.click_on_restore_button()
        restore.loading_field_for_code()
        restore.click_on_show_hide_button()

        assert restore.active_password_field()

