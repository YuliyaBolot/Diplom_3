from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.current_url = driver.current_url

    def go_to_site(self, url):
        return self.driver.get(url)

    def find_element_located(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(
            expected_conditions.presence_of_element_located(locator))

    def find_element_located_click(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(
            expected_conditions.element_to_be_clickable(locator)).click()
