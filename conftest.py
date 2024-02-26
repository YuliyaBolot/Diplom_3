from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest
import requests
from constants import APIConstants


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
    user = {
        "email": "Ilya92@yandex.ru",
        "password": "Il1992",
        "name": "Ilya"
    }
    response = requests.post(APIConstants.url_create_user, data=user)
    token = response.json()["accessToken"]
    yield prepare_user
    requests.delete(APIConstants.url_user, headers={'Authorization': token})



