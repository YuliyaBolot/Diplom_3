from selenium.webdriver.common.by import By


class RestorePasswordLocators:

    # Ссылка «Восстановить пароль»
    RESTORE_PASSWORD_LINK = (By.XPATH, ".//a[text() = 'Восстановить пароль']")

    # Страница восстановления пароля
    FORGOT_PASSWORD_PAGE = (By.XPATH, ".//div[@class = 'Auth_login__3hAey']/h2[text() = 'Восстановление пароля']")

    # Поле ввода email
    EMAIL_FIELD = (By.XPATH, ".//label[text() = 'Email']/following-sibling::input[@name = 'name']")

    # Кнопка «Восстановить»
    RESTORE_BUTTON = (By.CSS_SELECTOR, '.button_button_size_medium__3zxIa')

    # Поле ввода кода из письма
    FIELD_FOR_CODE = (By.XPATH, ".//label[text() = 'Введите код из письма']/following-sibling::input[@name = 'name']")

    # Кнопка показать/скрыть пораль
    SHOW_HIDE_BUTTON = (By.XPATH, ".//div[@class = 'input__icon input__icon-action']")

    # Поле для ввода пароля после нажатия на кнопку "показать/скрыть" пароль
    PASSWORD_FIELD = (By.CSS_SELECTOR, '.input_status_active')
