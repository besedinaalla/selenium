from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from osmohub_auto.osmohub_work.base.base_page import BasePage


# Класс страницы заявки
from osmohub_auto.osmohub_work.tests.data_tests import DataTest


class InquiryBuyerPage(BasePage):
    # url_dev = "https://dev.stroycode.ru/enquiries?page=1&perPage=10"
    # url_prod = "https://stroycode.ru/enquiries?page=1&perPage=10"
    # url_vert = "https://158.160.63.248/enquiries?page=1&perPage=10"

    def __init__(self, driver, url=DataTest.url+'/enquiries?page=1&perPage=10'):
        super().__init__(driver, url)
        self.driver = driver

    # Getters # Locators Локаторы элементов и получение этих элементов

# Окно формирования запроса

    # Поле Требуется доставка
    def get_yes_no_delivery(self):
        locator_yes_no_delivery = (By.XPATH, "//div[@class='field-depr']//input[@class='field-depr__input-tag']")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_yes_no_delivery))

    # Поле Грузополучатель
    def get_recipient(self):
        locator_recipient = (By.XPATH, "//input[@name='recipient']")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_recipient))

    # Поле Комментарий поставщику
    def get_comment(self):
        locator_comment = (By.XPATH, "//div[@class='field primary-field col-start-1 col-end-2']/textarea")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_comment))

    # Поле Отсрочка платежа
    def get_delay_payment(self):
        locator_delay_payment = (By.XPATH, "//input[@name='payment_deferment']")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_delay_payment))

    # Поле Поставщик
    def get_seller(self):
        locator_seller = (By.XPATH, "//input[@name='executor_ids']")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_seller))

    # Список поставщиков
    def get_sellers(self):
        locator_sellers = (By.XPATH, "//div[@id='executor_ids']//div[contains(@class,'dropdown__option')]")
        self.driver.implicitly_wait(DataTest.implicitly_wait)
        return self.driver.find_elements(*locator_sellers)

    # Выбор первого Поставщика
    def get_checkbox_seller(self):
        locator_checkbox_seller = (By.XPATH, "(//div[@id='executor_ids']//div[contains(@class,'dropdown__option')])[1]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_checkbox_seller))

    # Выбор первого Поставщика
    def get_checkbox_polyplastic(self):
        locator_checkbox_polyplastic = (By.XPATH, "//div[@id='executor_ids']//div[@id='1']")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_checkbox_polyplastic))

    # Название первого Поставщика в списке
    def get_name_seller(self):
        locator_name_seller = (By.XPATH, "(//div[@id='executor_ids']//div[contains(@class,'dropdown__option')]//p)[1]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_name_seller))

    # Название первого Поставщика в поле
    def get_name_choose_seller(self):
        locator_name_choose_seller = (By.XPATH, "(//div[@id='executor_ids']//span[@class='tag__title text-caption'])[1]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_name_choose_seller))

    # Выбор товарных позиций-список
    def get_checkbox_position(self):
        locator_checkbox_position = (By.XPATH, "//div[@class='table__row']//button[@class='btn-checkbox-primary btn-m text-btn-m btn-checkbox btn-only-icon']")
        self.driver.implicitly_wait(DataTest.implicitly_wait)
        return self.driver.find_elements(*locator_checkbox_position)

    # Наименования позиций, товарные категории, единицы измерения -список
    def get_positions(self):
        locator_positions = (By.XPATH, "//div[@class='table__row']//div[@class='truncate text-description']")
        self.driver.implicitly_wait(DataTest.implicitly_wait)
        return self.driver.find_elements(*locator_positions)

    # Количество по позициям-список
    def get_quantity(self):
        locator_quantity = (By.XPATH, "//div[@class='table__row']//input")
        self.driver.implicitly_wait(DataTest.implicitly_wait)
        return self.driver.find_elements(*locator_quantity)

    # Кнопка Послать запрос
    def get_send_inquiry(self):
        locator_send_inquiry = (By.XPATH, "//button[text()='Послать запрос']")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_send_inquiry))

# Вкладка запросы

    # Номер запроса
    def get_title_inquiry(self):
        locator_number_inquiry = (By.XPATH, "((//div[@id='enquiries-root']//div[@class='list-wrapper'])[2]//div[@class='item-cell__content'])[1]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_number_inquiry))

    # Имя покупателя во вкладке Запросы
    def get_buyer_inquiry(self):
        locator_buyer_inquiry = (By.XPATH, "((//div[@id='enquiries-root']//div[@class='list-wrapper'])[2]//div[@class='item-cell__content'])[2]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_buyer_inquiry))

    # Имя поставщика во вкладке Запросы
    def get_seller_inquiry(self):
        locator_seller_inquiry = (By.XPATH, "((//div[@id='enquiries-root']//div[@class='list-wrapper'])[2]//div[@class='item-cell__content'])[3]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_seller_inquiry))

    # Время размещения запроса
    def get_date_time_inquiry(self):
        locator_date_time_inquiry = (By.XPATH, "((//div[@id='enquiries-root']//div[@class='list-wrapper'])[2]//div[@class='item-cell__content'])[4]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_date_time_inquiry))

    # Статус счета
    def get_status_invoice(self):
        locator_status_invoice = (By.XPATH, "((//div[@id='enquiries-root']//div[@class='list-wrapper'])[2]//div[@class='item-cell__content'])[5]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_status_invoice))

    # Статус запроса
    def get_status_inquiry(self):
        locator_status_inquiry = (By.XPATH, "(//div[@id='enquiries-root']//div[@class='list-wrapper'])[2]//div[@class='item-cell__status-text']")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_status_inquiry))

# Вертикальное троеточие

    # Вертикальное троеточие
    def get_vertical_dots(self):
        locator_vertical_dots = (By.XPATH, "((//span[starts-with(text(),'Информация по заявке')]/parent::*)/parent::*)//button[contains(@class,'bg-transparent')]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_vertical_dots))

    # Информация
    def get_information(self):
        locator_information = (By.XPATH, "//div[text()='Информация']")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_information))

# Окно Информация по запросу

    # Поле Покупатель
    def get_buyer_info(self):
        locator_buyer = (By.XPATH, "//div[@class='informationOfInquiry']//div[contains(@class,'company')]/input")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.presence_of_element_located(locator_buyer))

    # Поле Грузополучатель
    def get_recipient_info(self):
        locator_recipient = (By.XPATH, "(//div[@class='informationOfInquiry']//div[contains(@class,'primary-field')])[2]/input")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_recipient))

    # Поле Требуется доставка
    def get_yes_no_delivery_info(self):
        locator_yes_no_delivery = (By.XPATH, "(//div[@class='informationOfInquiry']//div[contains(@class,'primary-field')])[3]/input")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_yes_no_delivery))

    # Поле адрес
    def get_address_info(self):
        locator_address = (By.XPATH, "//div[@class='informationOfInquiry']//div[contains(@class,'address')]/input")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_address))

    # Поле Отсрочка
    def get_delay_payment_info(self):
        locator_delay_payment = (By.XPATH, "(//div[@class='informationOfInquiry']//div[contains(@class,'primary-field')])[4]/input")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_delay_payment))

    # Поле Поставщик
    def get_seller_info(self):
        locator_seller = (By.XPATH, "(//div[@class='informationOfInquiry']//div[contains(@class,'primary-field')])[6]/input")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_seller))

    # Поле Комментарий
    def get_comment_info(self):
        locator_comment = (By.XPATH, "//div[@class='comment ']//p")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_comment))

    # Наименования, кол-во, категории,ед измерения товарных позиций
    def get_positions_info(self):
        locator_positions = (By.XPATH, "//div[@class='informationOfInquiry']//div[@class='table__row']//div[@class='truncate text-description']")
        self.driver.implicitly_wait(DataTest.implicitly_wait)
        return self.driver.find_elements(*locator_positions)

    # Методы

# Окно формирования запроса

    # Наименования товарных позиций список
    def get_names_positions(self):
        card_info = []
        for i in range(0, len(self.get_positions()), 3):
            card_info.append(self.get_positions()[i].text.lower())
        return card_info

    # Единицы измерения по позициям
    def get_units_positions(self):
        card_info = []
        for i in range(2, len(self.get_positions()), 3):
            card_info.append(self.get_positions()[i].text.lower())
        return card_info

    # Кол-во товаров по позициям
    def get_quantity_positions(self):
        card_info = []
        for i in self.get_quantity():
            card_info.append(i.get_attribute('value'))
        return sorted(card_info)

    # Выбрать все позиции
    def check_all_positions(self):
        for i in self.get_checkbox_position():
            # self.scroll_to_element(i)
            # time.sleep(0.5)
            self.click_element(i)

    # время создания запроса
    def datetime_create(self):
        return self.get_date_time_inquiry().text

# Окно Информации по запросу
    # Перейти во вкладку запросы
    def tab_info(self):
        self.click_element(self.get_vertical_dots())
        self.click_element(self.get_information())
        locator_loading_screen = (By.XPATH, "//div[@class='loadingScreen']")
        self.wait_loading(locator_loading_screen)

    # Наименования товарных позиций список
    def get_names_positions_info(self):
        card_info = []
        for i in range(0, len(self.get_positions_info()), 4):
            card_info.append(self.get_positions_info()[i].text.lower())
        return card_info

    # Единицы измерения
    def get_units_positions_info(self):
        card_info = []
        for i in range(2, len(self.get_positions_info()), 4):
            card_info.append(self.get_positions_info()[i].text.lower())
        return card_info

    # Кол-во товаров по позициям
    def get_quantity_positions_info(self):
        card_info = []
        for i in range(3, len(self.get_positions_info()), 4):
            card_info.append(self.get_positions_info()[i].text)
        return sorted(card_info)





