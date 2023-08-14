from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from osmohub_auto.osmohub_work.base.base_page import BasePage

# Класс главной страницы
from osmohub_auto.osmohub_work.pages.ssl_page import SslPage
from osmohub_auto.osmohub_work.tests.data_tests import DataTest


class MainPage(BasePage):
    # url_dev = DataTest.url_dev
    # url_prod = DataTest.url_prod
    # url_vert = "https://158.160.63.248"

    def __init__(self, driver, url=DataTest.url):
        super().__init__(driver, url)
        self.driver = driver

    # Getters # Locators Локаторы элементов и получение этих элементов

    # Лого
    def get_logo(self):
        locator_logo = (By.CLASS_NAME, 'top-navbar__logo')
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_logo))

    # Главная
    def get_main(self):
        locator_main = (By.XPATH, "//li[@class='top-navbar__menu__current-section']/a[text()='Главная']")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_main))

    # Каталог
    def get_catalog(self):
        locator_catalog = (By.XPATH, "//li[@class='top-navbar__menu__section']/a[text()='Каталог']")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_catalog))

    # Заявки
    def get_enquiries(self):
        locator_enquiries = (By.XPATH, "//li[@class='top-navbar__menu__section']/a[text()='Заявки']")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_enquiries))

    # Запросы
    def get_inquiries(self):
        locator_inquiries = (By.XPATH, "//li[@class='top-navbar__menu__current-section']/a[text()='Запросы']")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_inquiries))

    # Войти
    def get_login(self):
        locator_login = (By.XPATH, "//li[contains(@class,'registration')]/a[contains(text(),'Войти')]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_login))

    # Выход
    def get_logout(self):
        locator_logout = (By.XPATH, "//div[contains(@class,'logout')]//a")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_logout))

    # Кнопка закрытия дебаг меню на деве
    def get_debug_close_button(self):
        locator_debug_close_button = (By.XPATH, "//a[@class='phpdebugbar-close-btn']")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_debug_close_button))

    # кнопка куки
    def get_agree_cookie(self):
        locator_agree_cookie = (By.XPATH, "//button[contains(@class,'cookie-notice-buttonContainer__button')]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_agree_cookie))

    # Закрыть меню дебагера
    def close_debug(self):
        self.click_element(self.get_debug_close_button())

    # Согласиться с куки
    def agree_cookie(self):
        self.click_element(self.get_agree_cookie())

    # открыть страницу с проблемами в ssl, # закрыть страницу с дебагменю
    def open_page_ssl_debug(self):
        # открыть страницу с проблемами в ssl
        if 'stroycode' not in DataTest.url:
            self.open_page()
            if self.driver.name == 'chrome':
                SslPage(self.driver).sert()
            self.close_debug()
        else:
            if DataTest.url == 'https://stroycode.ru':
                self.open_page()
            else:
                self.open_page()
                self.close_debug()