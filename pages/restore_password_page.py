import allure
from pages.base_page import BasePage
from locators.restore_password_locators import RestorePasswordLocators


class RestorePasswordPage(BasePage):

    @allure.step("Нажимаем на ссылку 'Восстановить пароль'")
    def click_on_restore_password_link(self):
        return self.find_element_located_click(RestorePasswordLocators.RESTORE_PASSWORD_LINK)

    @allure.step("Загрузка страницы восстановления пароля")
    def loading_forgot_password_page(self):
        return self.find_element_located(RestorePasswordLocators.FORGOT_PASSWORD_PAGE)

    @allure.step("Вводим email")
    def set_email(self, email):
        return self.find_element_located(RestorePasswordLocators.EMAIL_FIELD).send_keys(email)

    @allure.step("Нажимаем на кнопку 'Восстановить'")
    def click_on_restore_button(self):
        return self.find_element_located_click(RestorePasswordLocators.RESTORE_BUTTON)

    @allure.step("Загрузка поля для ввода кода")
    def loading_field_for_code(self):
        return self.find_element_located(RestorePasswordLocators.FIELD_FOR_CODE)

    @allure.step("Нажимаем на кнопку показать/скрыть пароль")
    def click_on_show_hide_button(self):
        return self.find_element_located_click(RestorePasswordLocators.SHOW_HIDE_BUTTON)

    @allure.step("Активация поля для ввода пароля")
    def active_password_field(self):
        return self.find_element_located(RestorePasswordLocators.PASSWORD_FIELD)

