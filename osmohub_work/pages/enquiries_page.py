import time

from selenium.webdriver.support.expected_conditions import all_of
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from osmohub_auto.osmohub_work.base.base_page import BasePage


# Класс страницы заявки
from osmohub_auto.osmohub_work.tests.data_tests import DataTest


class EnquiriesPage(BasePage):
    # url_dev = "https://dev.stroycode.ru/enquiries?page=1&perPage=10"
    # url_prod = "https://stroycode.ru/enquiries?page=1&perPage=10"
    # url_vert = "https://158.160.63.248/enquiries?page=1&perPage=10"

    def __init__(self, driver, url=DataTest.url+'/enquiries?page=1&perPage=10'):
        super().__init__(driver, url)
        self.driver = driver

    # Getters # Locators Локаторы элементов и получение этих элементов

# Страница с заявками

    # Сортировка столбца Создана
    def get_sort_create(self):
        locator_sort_create = (By.XPATH, "//span[text()='Создана']/..//button[contains(@class,'content__sort-btn')]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_sort_create))

    # Наименование верхней заявки
    def get_title_first(self):
        locator_title_first = (By.XPATH, "(//div[@id='enquiries-root']//div[@class='list-wrapper']//div[@class='item-cell__content'])[1]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_title_first))

    # Дата верхней заявки
    def get_date_first(self):
        locator_date_last = (By.XPATH, "(//div[@id='enquiries-root']//div[@class='list-wrapper']//div[contains(@class, 'items-start')]/span[1])[1]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_date_last))

    # Время верхней заявки
    def get_time_first(self):
        locator_time_last = (By.XPATH, "(//div[@id='enquiries-root']//div[@class='list-wrapper']//div[contains(@class, 'items-start')]/span[2])[1]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_time_last))

    # Кол-во позиций  в верхней заявке
    def get_number_positions_first(self):
        locator_number_positions = (By.XPATH, "(//div[@id='enquiries-root']//div[@class='list-wrapper']//div[contains(@class,'positions-item-cell')]/div)[1]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_number_positions))

    # Статус верхней заявки
    def get_enquiry_status_first(self):
        locator_enquiry_status = (By.XPATH, "(//div[@id='enquiries-root']//div[@class='list-wrapper']//div[contains(@class,'status-text')])[1]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_enquiry_status))

    # Чек-бокс верхней заявки
    def get_checkbox_enquiry_first(self):
        locator_checkbox_enquiry = (By.XPATH, "(//div[@id='enquiries-root']//div[@class='list-wrapper']//div[@class='item-cell checkbox-item-cell']//button)[1]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_checkbox_enquiry))

    # Кнопка Отправить запрос
    def get_send_inquiry(self):
        locator_send_inquiry = (By.XPATH, "//button[text()='Отправить запрос']")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_send_inquiry))

# Вертикальное троеточие

    # Вертикальное троеточие
    def get_vertical_dots(self):
        locator_vertical_dots = (By.XPATH, "(//div[@id='enquiries-root']//div[@class='list-wrapper']//button[contains(@class,'bg-transparent')])[1]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_vertical_dots))

    # Информация по заявке
    def get_information(self):
        locator_information = (By.XPATH, "(//div[text()='Информация по заявке'])[1]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_information))

    # Открыть счет
    def get_open_invoice(self):
        locator_open_invoice = (By.XPATH, "(//div[text()='Открыть счет'])[1]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_open_invoice))

# Окно информация по заявке

    # вкладка Позиции (вся информация из таблицы в списке)
    def get_positions(self):
        locator_positions = (By.XPATH, "//div[@class='enquiry-products h-full']//div[@class='table__rows-wrapper']//div[@class='truncate text-description']")
        self.driver.implicitly_wait(DataTest.implicitly_wait)
        return self.driver.find_elements(*locator_positions)

    locator_loading_screen = (By.XPATH, "//div[@class='loadingScreen']")

    def get_loading_screen(self):
        locator_loading_screen = (By.XPATH, "//div[@class='loadingScreen']")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.invisibility_of_element_located(locator_loading_screen))

    # Вкладка запросы
    def get_tab_inquiries(self):
        locator_tab_inquiries = (By.XPATH, "//div[contains(@class,'tab-selector')]//span[text()='Запросы']")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_tab_inquiries))

    # Выход из Информации по заявке
    def get_exit_information(self):
        locator_exit_information = (By.XPATH, "//span[starts-with(text(),'Информация по заявке')]/parent::*/button")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_exit_information))

# методы
# страница с заявками

    # сортировка по столбцу Создана
    def sort_create(self):
        self.click_element(self.get_sort_create())

    # время создания заявки
    def datetime_create(self):
        return self.get_date_first().text + ' ' + self.get_time_first().text

# окно информации по заявке

    # Наименования товарных позиций список
    def get_names_positions(self):
        card_info = []
        for i in range(0, len(self.get_positions()), 3):
            card_info.append(self.get_positions()[i].text.lower())
        return card_info

    # Кол-во товаров по позициям
    def get_quantity_positions(self):
        card_info = []
        for i in range(2, len(self.get_positions()), 3):
            card_info.append(self.get_positions()[i].text)
        return sorted(card_info)

    # Перейти во вкладку запросы
    def tab_inquiries(self):
        self.click_element(self.get_vertical_dots())
        self.click_element(self.get_information())
        locator_loading_screen = (By.XPATH, "//div[@class='loadingScreen']")
        self. wait_loading(locator_loading_screen)
        self.click_element(self.get_tab_inquiries())
