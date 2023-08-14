# импорт класса страницы авторизации

import pytest

from osmohub_auto.osmohub_work.pages.catalog_page import CatalogPage
from osmohub_auto.osmohub_work.pages.login_page import LoginPage
from osmohub_auto.osmohub_work.pages.ssl_page import SslPage

login_correct_buyer = "Test1CD2@remkis.ru"
password_correct_buyer = 'dSw[`r8d1d]"`#;'
login_incorrect = "Test1@remkis.ru"
password_incorrect = 'dSw[`r8d1d]"`#;123'
login_not_email = "kjuyy654!#$!"

login_correct_dev = "test_buyer@osmocode.ru"
password_correct_dev = 'qwerty1234'


@pytest.mark.usefixtures("driver_init")
class TestLogin:
    def test_login_positive(self):
        page = LoginPage(self.driver)
        page.open_page()
        if self.driver.name == 'chrome':
            SslPage(self.driver).sert()
        page.authorization(login_correct_buyer, password_correct_buyer)
        # page.get_screenshot()
        CatalogPage(self.driver).assert_url_is_current()
        print("Позитивный тест авторизации пройден")
    #
    # def test_login_negative_empty_fields(self):
    #     page = LoginPage(self.driver)
    #     page.authorization('', '')
    #     page.assert_url_is_current()
    #     page.assert_notification(page.get_notification(), "Поле email адрес обязательно для заполнения.")
    #     print("Тест авторизации (поля не заполнены) пройден")
    #
    # def test_login_negative_empty_email(self):
    #     page = LoginPage(self.driver)
    #     page.authorization('', password_correct)
    #     page.assert_url_is_current()
    #     page.assert_notification(page.get_notification(), "Поле email адрес обязательно для заполнения.")
    #     print("Тест авторизации (поле 'Email' не заполненo) пройден")
    #
    # def test_login_negative_empty_password(self):
    #     page = LoginPage(self.driver)
    #     page.authorization(login_correct_buyer, '')
    #     page.assert_url_is_current()
    #     page.assert_notification(page.get_notification(), "Поле пароль обязательно для заполнения.")
    #     print("Тест авторизации (поле 'Пароль' не заполненo) пройден")
    #
    # def test_login_negative_incorrect_password(self):
    #     page = LoginPage(self.driver)
    #     page.authorization(login_correct_buyer, password_incorrect_buyer)
    #     page.assert_url_is_current()
    #     page.assert_notification(page.get_notification(), "Неверное имя пользователя или пароль.")
    #     print("Тест авторизации (некорректный 'Пароль') пройден")
    #
    # def test_login_negative_incorrect_email(self):
    #     page = LoginPage(self.driver)
    #     page.authorization(login_incorrect, password_correct_buyer)
    #     page.assert_url_is_current()
    #     page.assert_notification(page.get_notification(), "Неверное имя пользователя или пароль.")
    #     print("Тест авторизации (некорректный 'Email') пройден")
    #
    # def test_login_negative_not_email(self):
    #     page = LoginPage(self.driver)
    #     page.authorization(login_not_email, password_correct_buyer)
    #     page.assert_url_is_current()
    #     page.assert_notification(page.get_notification(),
    #                              "Поле email адрес должно быть действительным электронным адресом.")
    #     print("Тест авторизации (некорректный 'Email' (неправильный формат)) пройден")
    #
    # def test_login_negative_incorrect(self):
    #     page = LoginPage(self.driver)
    #     page.authorization(login_incorrect, password_incorrect)
    #     page.assert_url_is_current()
    #     page.assert_notification(page.get_notification(), "Неверное имя пользователя или пароль.")
    #     print("Тест авторизации (поле 'Email' и 'Пароль' некорректны) пройден")
    #
    # def test_login_eye(self):
    #     page = LoginPage(self.driver)
    #     page.open_page()
    #     if self.driver.name == 'chrome':
    #         page_ssl = SslPage(self.driver)
    #         page_ssl.https()
    #     page.assert_eye(page.get_password(), password_incorrect, page.get_eye())
    #     print("Тест иконки 'Глазик' пройден")
    #
    # def test_login_clear_email(self):
    #     page = LoginPage(self.driver)
    #     if self.driver.name == 'chrome':
    #         page_ssl = SslPage(self.driver)
    #         page_ssl.https()
    #     page.assert_clear_field(page.get_email(), page.get_clear_field(login_not_email))
    #     print("Тест очистки поля 'Email' пройден")
