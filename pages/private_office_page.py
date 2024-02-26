from pages.base_page import BasePage
from locators.private_office_locators import PrivateOfficeLocators


class PrivateOfficePage(BasePage):

    def loading_login_page(self):
        return self.find_element_located(PrivateOfficeLocators.LOGIN_PAGE)

    def set_email(self, email):
        return self.find_element_located(PrivateOfficeLocators.EMAIL_FIELD).send_keys(email)

    def set_password(self, password):
        return self.find_element_located(PrivateOfficeLocators.PASSWORD_FIELD).send_keys(password)

    def click_on_enter_button(self):
        return self.find_element_located_click(PrivateOfficeLocators.ENTER_BUTTON)

    def loading_profile_page(self):
        return self.find_element_located(PrivateOfficeLocators.PRIVATE_OFFICE_PAGE)

    def login_to_private_account(self, email, password):
        self.loading_login_page()
        self.set_email(email)
        self.set_password(password)
        self.click_on_enter_button()

    def click_on_history_order(self):
        return self.find_element_located_click(PrivateOfficeLocators.HISTORY_ORDER)

    def loading_history_order_page(self):
        return self.find_element_located(PrivateOfficeLocators.HISTORY_ORDER_PAGE)

    def go_to_history_order(self):
        self.click_on_history_order()
        self.loading_history_order_page()

    def click_on_exit_button(self):
        return self.find_element_located_click(PrivateOfficeLocators.EXIT_BUTTON)
