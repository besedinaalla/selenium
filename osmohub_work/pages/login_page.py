from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from osmohub_auto.osmohub_work.base.base_page import BasePage


# Класс страницы авторизации
from osmohub_auto.osmohub_work.tests.data_tests import DataTest


class LoginPage(BasePage):
    # url_dev = "https://dev.stroycode.ru/login"
    # url_prod = "https://stroycode.ru/login"
    # url_vert = "https://158.160.63.248/login"

    def __init__(self, driver, url=DataTest.url+'/login'):
        super().__init__(driver, url)
        self.driver = driver

    # Getters  # Locators Локаторы элементов и получение этих элементов
    # Поле Логин
    def get_email(self):
        locator_login = (By.NAME, 'email')
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_login))

    # Поле Пароль
    def get_password(self):
        locator_password = (By.NAME, 'password')
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_password))

    # Кнопка Авторизоваться
    def get_button_login(self):
        locator_button_login = (By.CSS_SELECTOR, "button[type=submit]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_button_login))

    # Чек-бокс Запомнить меня
    def get_remember(self):
        locator_checkbox_remember = (By.XPATH, "//div[@class='remember-me']/label")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_checkbox_remember))

    # Иконка "Глазик"
    def get_eye(self):
        locator_eye = (By.XPATH, "//button[@class='field-wrapper__btn']")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_eye))

    # Ссылка Забыли пароль?
    def get_forgot_password(self):
        locator_forgot = (By.XPATH, "//div[@class='forgot-password-container']/a")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_forgot))

    # Сообщение об ошибке
    def get_notification_email(self):
        locator_notification_email = (By.XPATH, "//div[@class='input-container notification-under']//span[@class ='mini-notification__text text-body-3']")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.visibility_of_element_located(locator_notification_email))

    def get_notification_password(self):
        locator_notification_password = (By.XPATH, "//div[@class='input-container password-container notification-under']//span[@class ='mini-notification__text text-body-3']")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.visibility_of_element_located(locator_notification_password))

    # Кнопка очистки поля логина Х после заполнения
    def get_clear_field(self, login):
        self.input_field(self.get_email(), login)
        locator_clear_field = (By.XPATH, "//button[@class='field__btn']")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_clear_field))

    # Методы
    # Авторизация
    def authorization(self, login, password):
        self.input_field(self.get_email(), login)
        self.input_field(self.get_password(), password)
        self.click_element(self.get_remember())
        self.click_element(self.get_button_login())

    # Method Assert Eye проверка иконки "Глаз"
    def assert_eye(self, get_password, password, get_eye):
        self.input_field(get_password, password)
        self.click_element(get_eye)
        self.get_screenshot()
        self.assert_value_attribute(get_password, 'type', 'text')
        self.click_element(get_eye)
        self.get_screenshot()
        self.assert_value_attribute(get_password, 'type', 'password')
