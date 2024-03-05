from selenium.webdriver.common.by import By


class PrivateOfficeLocators:

    # Страница входа в личный кабинет
    LOGIN_PAGE = (By.XPATH, ".//main//h2[text() = 'Вход']")

    # Страница личного кабинета
    PRIVATE_OFFICE_PAGE = (By.CLASS_NAME, "Profile_profile__3dzvr")

    # Кнопка «Войти» для входа в аккаунт
    ENTER_BUTTON = (By.XPATH, ".//form/button[text() = 'Войти']")

    # Поля входа в личный кабинет
    EMAIL_FIELD = (By.XPATH, ".//label[text() = 'Email']/following-sibling::input[@name = 'name']")
    PASSWORD_FIELD = (By.XPATH, ".//label[text() = 'Пароль']/following-sibling::input[@name = 'Пароль']")

    # Кнопка «Выйти» из аккаунта
    EXIT_BUTTON = (By.XPATH, ".//li[@class = 'Account_listItem__35dAP']/button[text() = 'Выход']")

    # История заказов
    HISTORY_ORDER = (By.XPATH, ".//li[@class = 'Account_listItem__35dAP']/a[@href = '/account/order-history']")

    # Страница истории заказов
    HISTORY_ORDER_PAGE = (By.CLASS_NAME, 'App_componentContainer__2JC2W')
