import datetime
import time


# Базовый класс, который содержит все используемые методы для тестов
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    # инициализируем класс
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    # Method Open Page открытие страницы по url
    def open_page(self):
        self.driver.get(self.url)

    # Method Get Current Url получение адреса страницы
    def get_current_url(self):
        return self.driver.current_url

    # Method Save Screenshot сохранение скриншота
    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime('%Y-%m-%d %H-%M-%S')
        name_screenshot = 'screen ' + now_date + '.png'
        time.sleep(1)
        self.driver.save_screenshot('..\\screen\\' + name_screenshot)

    # Method Input Element заполнение поля
    def input_field(self, element, data):
        element.send_keys(data)

    # Method Click Element нажатие элемента
    def click_element(self, element):
        element.click()

    # Method Scroll to element скролл до элемента
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(false);", element)

    # Method скрыть аттрибут хидден, чтоб элемент был виден на странице
    def clear_hidden(self, element):
        self.driver.execute_script("arguments[0].removeAttribute('hidden');", element)

    # Method Assert Url проверка соотвествия адреса страницы
    def assert_url(self, expected_url):
        actual_url = self.get_current_url()
        assert actual_url == expected_url, f"Ожидалась страница {expected_url}: {actual_url}"

    def assert_url_is_current(self):
        assert self.url == self.get_current_url(), f"Ожидалась страница {self.url}: {self.get_current_url()}"

    # Method Assert Text проверка текста в элементе
    def assert_text(self, actual_text_element, expected_text):
        actual_text = actual_text_element.text
        assert actual_text == expected_text, f"Ожидался текст {expected_text}: {actual_text}"

    def assert_time_in_range(self, actual_datetime, expected_datetime1, expected_datetime2):
        # actual_time = actual_date_element.text +" "+actual_time_element.text
        assert actual_datetime >= expected_datetime1 and actual_datetime <= expected_datetime2, f"Ожидалось время между {expected_datetime1} и {expected_datetime2}: {actual_datetime}"

    # Method Assert Value Attribute проверка значения аттрибута элемента
    def assert_value_attribute(self, element, attribute, expected_value):
        value_attribute = element.get_attribute(attribute)
        assert value_attribute == expected_value, f"Ожидалось значение аттрибута {expected_value}: " \
                                                  f"{value_attribute}"

    #  Method Assert Notification проверка сообщения об ошибке
    def assert_notification(self, actual_notification, expected_notification):
        self.get_screenshot()
        self.assert_text(actual_notification, expected_notification)

    # Method Asser Clear Field проверка очистки поля через Х
    def assert_clear_field(self, input_element, get_clear_field):
        self.click_element(get_clear_field)
        self.assert_value_attribute(input_element, 'value', '')

    # Проверка элементы одного списка есть в другом списке
    def assert_items_of_list(self, actual_list, expected_list):
        for item in expected_list:
            assert item in actual_list, f"Товара {item} нет в проверяемом списке"

    # Проверка 2 списков
    def assert_lists(self, actual_list, expected_list):
        assert actual_list == expected_list, f"Ожидалось  {expected_list}: " \
                                                  f"{actual_list}"

    def wait_loading(self, locator):
        """Процесс загрузки"""
        while True:
            try:
                WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(locator))
            except TimeoutException:
                return
            WebDriverWait(self.driver, 500).until(EC.invisibility_of_element_located(locator))

