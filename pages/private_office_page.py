import allure
from pages.base_page import BasePage
from locators.private_office_locators import PrivateOfficeLocators


class PrivateOfficePage(BasePage):

    @allure.step("Загрузка страницы входа в личный кабинет")
    def loading_login_page(self):
        return self.find_element_located(PrivateOfficeLocators.LOGIN_PAGE)

    @allure.step("Вводим email")
    def set_email(self, email):
        return self.find_element_located(PrivateOfficeLocators.EMAIL_FIELD).send_keys(email)

    @allure.step("Вводим пароль")
    def set_password(self, password):
        return self.find_element_located(PrivateOfficeLocators.PASSWORD_FIELD).send_keys(password)

    @allure.step("Нажимаем на кнопку 'Войти'")
    def click_on_enter_button(self):
        return self.find_element_located_click(PrivateOfficeLocators.ENTER_BUTTON)

    @allure.step("Загрузка страницы личного кабинета")
    def loading_profile_page(self):
        return self.find_element_located(PrivateOfficeLocators.PRIVATE_OFFICE_PAGE)

    @allure.step("Нажимаем на кнопку 'История заказов'")
    def click_on_history_order(self):
        return self.find_element_located_click(PrivateOfficeLocators.HISTORY_ORDER)

    @allure.step("Загрузка страницы с историей заказов пользователя")
    def loading_history_order_page(self):
        return self.find_element_located(PrivateOfficeLocators.HISTORY_ORDER_PAGE)

    @allure.step("Переходим на страницу истории заказов пользователя")
    def go_to_history_order(self):
        self.click_on_history_order()
        self.loading_history_order_page()

    @allure.step("Нажимаем на кнопку 'Выход'")
    def click_on_exit_button(self):
        return self.find_element_located_click(PrivateOfficeLocators.EXIT_BUTTON)
