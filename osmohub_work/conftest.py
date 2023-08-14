# импортируем модуль pytest
import pytest

# импортируем webdriver из модуля selenium
from selenium import webdriver

# Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Firefox
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.firefox import GeckoDriverManager
import os
# Edge
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# os.environ['WDM_SSL_VERIFY'] = '0'


# фикстура: открываем браузер перед выполнением теста и закрываем после, исходя из параметров инициализируем хром или фф
@pytest.fixture(params=["chrome"])
def driver_init(request):
    if request.param == "chrome":
        options = Options()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(version="114.0.5735.90").install()),
                                  options=options)
    if request.param == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    request.cls.driver = driver
    print(driver.name)
    driver.set_window_size(1920, 1080)
    # driver.maximize_window()
    yield
    driver.quit()
