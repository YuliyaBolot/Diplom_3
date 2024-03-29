from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest
import requests
from constants import APIUrls, Data, Urls
from locators.private_office_locators import PrivateOfficeLocators


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        options = Options()
        options.add_argument("--window-size=1400,1800")
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif request.param == 'firefox':
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)

    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def prepare_user():
    user = Data.data_register
    response = requests.post(APIUrls.url_create_user, data=user)
    token = response.json()["accessToken"]
    yield prepare_user
    requests.delete(APIUrls.url_user, headers={'Authorization': token})


@pytest.fixture(scope='function')
def login_user(driver):
    user = Data.data_login
    driver.get(Urls.URL_LOGIN)
    driver.find_element(*PrivateOfficeLocators.EMAIL_FIELD).send_keys(user["email"])
    driver.find_element(*PrivateOfficeLocators.PASSWORD_FIELD).send_keys(user["password"])
    driver.find_element(*PrivateOfficeLocators.ENTER_BUTTON).click()






