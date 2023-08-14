from selenium.webdriver.common.by import By
from osmohub_auto.osmohub_work.base.base_page import BasePage
from osmohub_auto.osmohub_work.tests.data_tests import DataTest


class SslPage(BasePage):
    # url_vert = "https://158.160.63.248/login"

    def __init__(self, driver, url=DataTest.url):
        super().__init__(driver, url)
        self.driver = driver

    # Обходим проблемы с сертификатом
    def sert(self):
        # Chrome
        button = self.driver.find_element(By.CSS_SELECTOR, "#details-button.secondary-button")
        self.click_element(button)
        link1 = self.driver.find_element(By.CSS_SELECTOR, "#proceed-link.small-link")
        self.click_element(link1)
        # FireFox
        # button1 = self.browser.find_element(By.CSS_SELECTOR, "#advancedButton")
        # button1.click()
        # button2 = self.browser.find_element(By.CSS_SELECTOR, "#exceptionDialogButton")
        # button2.click()
