import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class BasePage:

    @allure.step("Инициализируем драйвер")
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открываем страницу {url}")
    def go_to_site(self, url):
        return self.driver.get(url)

    @allure.step("Находим элемент")
    def find_element_located(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(
            expected_conditions.presence_of_element_located(locator))

    @allure.step("Ожидаем возможности нажатия на элемент")
    def find_element_located_click(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(
            expected_conditions.element_to_be_clickable(locator)).click()

    @allure.step("Добавляем ингредиент в заказ")
    def drag_and_drop(self, locator_take, locator_put):
        return ActionChains(self.driver).drag_and_drop(self.find_element_located(locator_take),
                                                       self.find_element_located(locator_put)).perform()

    @allure.step("Получаем текущую страницу приложения")
    def current_url(self):
        return self.driver.current_url

