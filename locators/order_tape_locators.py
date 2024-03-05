from selenium.webdriver.common.by import By


class OrderTapeLocators:

    # Страница заказов
    ORDER_PAGE = (By.CLASS_NAME, 'OrderFeed_orderFeed__2RO_j')

    # Заказ
    ORDER = (By.XPATH, ".//a[@class = 'OrderHistory_link__1iNby']")

    # Окно с деталями заказа
    ORDER_WINDOW = (By.CSS_SELECTOR, '.p-10')

    # Информация о составе заказа
    ORDER_COMPOSITION = (By.XPATH, ".//p[@class = 'text text_type_main-medium mb-8']")

    # Номер заказа
    ORDER_NUMBER = (By.XPATH, ".//a[@class = 'OrderHistory_link__1iNby']//p[@class = 'text text_type_digits-default']")

    # Счетчик всех заказов
    COUNTER_ALL_ORDERS = (By.XPATH, ".//p[text() = 'Выполнено за все время:']/following-sibling::p[@class = 'OrderFeed_number__2MbrQ text text_type_digits-large']")

    # Счетчик заказов на сегодня
    COUNTER_TODAY_ORDERS = (By.XPATH, ".//p[text() = 'Выполнено за сегодня:']/following-sibling::p[@class = 'OrderFeed_number__2MbrQ text text_type_digits-large']")

    # Номер заказа из раздела "в работе"
    NUMBER_IN_PROGRESS = (By.XPATH, ".//li[@class = 'text text_type_main-small']")

    # Номер заказа из всплывающего окна при оформлении
    NUMBER_FROM_POP_UP = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title__2L34m')]")


