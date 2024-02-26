from pages.base_page import BasePage
from locators.restore_password_locators import RestorePasswordLocators


class RestorePasswordPage(BasePage):

    def click_on_restore_password_link(self):
        return self.find_element_located_click(RestorePasswordLocators.RESTORE_PASSWORD_LINK)

    def loading_forgot_password_page(self):
        return self.find_element_located(RestorePasswordLocators.FORGOT_PASSWORD_PAGE)

    def set_email(self, email):
        return self.find_element_located(RestorePasswordLocators.EMAIL_FIELD).send_keys(email)

    def click_on_restore_button(self):
        return self.find_element_located_click(RestorePasswordLocators.RESTORE_BUTTON)

    def loading_field_for_code(self):
        return self.find_element_located(RestorePasswordLocators.FIELD_FOR_CODE)

    def click_on_show_hide_button(self):
        return self.find_element_located_click(RestorePasswordLocators.SHOW_HIDE_BUTTON)

    def active_password_field(self):
        return self.find_element_located(RestorePasswordLocators.PASSWORD_FIELD)

