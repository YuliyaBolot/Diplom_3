from selenium.webdriver.common.by import By


class MainLocators:

    # Главная страница приложения
    MAIN_PAGE = (By.XPATH, ".//main[@class = 'App_componentContainer__2JC2W']")

    # Кнопка входа в «Личный кабинет»
    PRIVATE_OFFICE_BUTTON = (By.XPATH, ".//a[@class ='AppHeader_header__link__3D_hX']/p[text()='Личный Кабинет']")

    # Кнопка «Конструктор»
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//li/a[@href= '/']")

    # Лента Заказов
    ORDERS_TAPE = (By.XPATH, ".//li[@class = 'undefined ml-2']/a[@href = '/feed']")

    # Страница заказов
    ORDER_PAGE = (By.CLASS_NAME, 'OrderFeed_orderFeed__2RO_j')

    # Список ингредиентов
    INGREDIENT_LST = (By.CLASS_NAME, 'BurgerIngredients_ingredients__1N8v2')

    # Ингредиенты
    INGREDIENT = (By.XPATH, ".//img[@alt = 'Мясо бессмертных моллюсков Protostomia']")
    INGREDIENT_BUN = (By.XPATH, ".//img[@alt = 'Флюоресцентная булка R2-D3']")

    # Счетчик ингредиента
    COUNT_INGREDIENT = (By.XPATH, ".//a[@href = '/ingredient/61c0c5a71d1f82001bdaaa6f']//p[@class = 'counter_counter__num__3nue1']")

    # Всплывающее окно
    POP_UP_WINDOW = (By.CLASS_NAME, 'Modal_modal__container__Wo2l_')

    # Закрытие всплывающего окна
    CLOSE_POP_UP_WINDOW = (By.CSS_SELECTOR, '.Modal_modal__close__TnseK')

    # Закрытое окно ингредиента
    CLOSE_INGREDIENT_DETAILS = (By.CLASS_NAME, 'Modal_modal__P3_V5')

    # Корзина заказa
    ORDER_BASKET = (By.XPATH, ".//ul[@class = 'BurgerConstructor_basket__list__l9dp_']")

    # Место ингредиента в корзине
    PLACE_FOR_INGREDIENT = (By.XPATH, ".//span[@class = 'BurgerConstructor_basket__listContainer__3P_AM']")

    # Кнопка оформления заказа
    CREATE_ORDER_BUTTON = (By.CSS_SELECTOR, '.button_button_size_large__G21Vg')



