import time
from random import random, uniform, randint

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from osmohub_auto.osmohub_work.base.base_page import BasePage


# Класс страницы заявки
from osmohub_auto.osmohub_work.tests.data_tests import DataTest


class InquirySellerPage(BasePage):


    def __init__(self, driver, url=DataTest.url+'/inquiries?page=1&perPage=10'):
        super().__init__(driver, url)
        self.driver = driver

    # Getters # Locators Локаторы элементов и получение этих элементов

# Страница с запросами
    # Сортировка столбца Размещено
    def get_sort_create(self):
        locator_sort_create = (By.XPATH, "//span[text()='Размещено']/..//button[contains(@class,'content__sort-btn')]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_sort_create))

    # Наименование верхнего запроса
    def get_name_first(self):
        locator_name_first = (By.XPATH, "(//div[@id='inquiries-root']//div[contains(@class, 'item-cell__content')])[1]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_name_first))

    # Дата и время верхнего запроса (Размещено)
    def get_datetime_first(self):
        locator_datetime_last = (By.XPATH, "(//div[@id='inquiries-root']//div[contains(@class, 'item-cell__content')])[5]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_datetime_last))

    # Кол-во позиций  в верхнем запросе
    def get_number_positions(self):
        locator_number_positions = (By.XPATH, "(//div[@id='inquiries-root']//div[contains(@class, 'item-cell__content')])[4]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_number_positions))

    # Наименование создателя верхнего запроса
    def get_buyer_first(self):
        locator_buyer_first = (By.XPATH, "(//div[@id='inquiries-root']//div[contains(@class, 'item-cell__content')])[2]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_buyer_first))

    # Наименование исполнителя верхнего запроса
    def get_seller_first(self):
        locator_seller_first = (By.XPATH, "(//div[@id='inquiries-root']//div[contains(@class, 'item-cell__content')])[3]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_seller_first))

    # Статус счета верхнего запроса
    def get_invoice_status(self):
        locator_invoice_status = (By.XPATH, "(//div[@id='inquiries-root']//div[contains(@class, 'item-cell__content')])[6]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_invoice_status))

    # Статус верхнего запроса
    def get_inquiry_status(self):
        locator_inquiry_status = (By.XPATH, "(//div[@id='inquiries-root']//div[@class='item-cell__status-text'])[1]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_inquiry_status))

    # Чек-бокс верхнего запроса
    def get_checkbox_inquiry(self):
        locator_checkbox_inquiry = (By.XPATH, "(//div[@class='item-cell checkbox-item-cell']//button)[1]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_checkbox_inquiry))

    # Кнопка Отправить счет
    def get_send_invoice(self):
        locator_send_invoice = (By.XPATH, "//div[@class='inquiries-head']//button[text()='Отправить счет']")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_send_invoice))

# Страница создания счета

    # Выбор типа доставки
    def get_radio_no_delivery(self):
        locator_radio_no_delivery = (By.XPATH, "//div[contains(@class,'radio')]//input[@value='2']")
        # locator_radio_no_delivery = (By.XPATH, "(//span[@class='radio__label'])[3]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.presence_of_element_located(locator_radio_no_delivery))

    # Поле Номер счета
    def get_title(self):
        locator_title = (By.XPATH, "//input[@name='title']")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_title))

    # Поле Адрес самовывоза
    def get_address(self):
        locator_address = (By.XPATH, "//input[@name='delivery_address_id']")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_address))

    # Выпадающий список
    def get_dropdown_address(self):
        locator_get_dropdown_address = (By.XPATH,
                                        "//div[contains(@class,'add-delivery-address')]//div[@class='elevation-1 typeahead-depr__dropdown']")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_get_dropdown_address))

    # Адрес из выпадающего списка
    def get_address_from_dropdown(self):
        locator_get_address_from_dropdown_ = (By.XPATH, "//div[contains(@class,'dropdown__option')][1]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_get_address_from_dropdown_))

    # Поле предоплата
    def get_prepayment(self):
        locator_prepayment = (By.XPATH, "//input[@name='prepayment']")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_prepayment))

    # Поле отсрочка
    def get_payment_deferment(self):
        locator_payment_deferment = (By.XPATH, "//input[@name='payment_deferment']")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_payment_deferment))

    # Прикрепление файла
    def get_file(self):
        locator_file = (By.XPATH, "//div[@class='w-full h-full']//input")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.presence_of_element_located(locator_file))

    # Прикрепленный файл
    def get_title_file(self):
        locator_title_file = (By.XPATH, "//div[@class='tags-group']//div[contains(@class,'tag')][1]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_title_file))

    # Чек-бокс выбора позиций
    def get_checkbox_position(self):
        locator_checkbox_position = (By.XPATH,
                                     "//div[@class='table__row']//button[@class='btn-checkbox-primary btn-m text-btn-m btn-checkbox btn-only-icon']")
        self.driver.implicitly_wait(DataTest.implicitly_wait)
        return self.driver.find_elements(*locator_checkbox_position)

    # Наименования позиций, товарные категории, единицы измерения -список
    def get_positions(self):
        locator_positions = (By.XPATH, "//div[@class='table__row']//div[@class='truncate text-description']")
        self.driver.implicitly_wait(DataTest.implicitly_wait)
        return self.driver.find_elements(*locator_positions)

    # Количество по позициям-список
    def get_quantity(self):
        locator_quantity = (By.XPATH, "//div[@class='table__row']//div[contains(@class,'editable-body-row-cell')]//input")
        self.driver.implicitly_wait(DataTest.implicitly_wait)
        return self.driver.find_elements(*locator_quantity)

    # Поля Цена
    def get_price(self):
        locator_price = (By.XPATH, "//div[@class='table__row']//div[contains(@class,'input-body-row-cell')]//input")
        self.driver.implicitly_wait(DataTest.implicitly_wait)
        return self.driver.find_elements(*locator_price)

    # Кнопка Отправить счет
    def get_send_invoice_2(self):
        locator_send_invoice_2 = (By.XPATH, "//form//button[text()='Отправить счет']")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_send_invoice_2))

    # Кнопка Отправить в окне подтверждения
    def get_send_notification(self):
        locator_send_notification = (By.XPATH, "//div[@class='card-notification']//button[text()='Отправить']")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_send_notification))

# Вертикальное троеточие

    # Вертикальное троеточие
    def get_vertical_dots(self):
        locator_vertical_dots = (By.XPATH, "(//button[contains(@class,'bg-transparent')])[1]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_vertical_dots))

    # Информация по запросу
    def get_information(self):
        locator_information = (By.XPATH, "(//div[text()='Информация'])[1]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_information))

    # Посмотреть счет
    def get_look_invoice_dots(self):
        locator_look_invoice = (By.XPATH, "(//div[text()='Посмотреть счет'])[1]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_look_invoice))

# Страница Информация по запросу

    # Поле Покупатель,компания
    def get_buyer_info(self):
        locator_yes_no_delivery = (By.XPATH, "//div[@class='informationOfInquiry']//div[contains(@class,'company')]/input")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_yes_no_delivery))

    # Поле Требуется доставка
    def get_yes_no_delivery_info(self):
        locator_yes_no_delivery = (By.XPATH, "(//div[@class='informationOfInquiry']//div[contains(@class,'primary-field')])[3]/input")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_yes_no_delivery))

    # Поле адрес
    def get_address_info(self):
        locator_address = (By.XPATH, "//div[@class='informationOfInquiry']//div[contains(@class,'address')]/input")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_address))

    # Поле Грузополучатель
    def get_recipient_info(self):
        locator_recipient = (By.XPATH, "(//div[@class='informationOfInquiry']//div[contains(@class,'primary-field')])[2]/input")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_recipient))

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

    # Выход из Информации по запросу
    def get_exit_information(self):
        locator_exit_information = (By.XPATH, "//span[starts-with(text(),'Запрос')]/parent::*/button")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_exit_information))

# Страница посмотреть счет

    # вкладка Посмотреть счет
    def get_look_invoice(self):
        locator_look_invoice = (By.XPATH, "//span[text()='Посмотреть счет']/parent::*")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_look_invoice))

    # Выбор типа доставки
    def get_radio_no_delivery_invoice(self):
        locator_radio_no_delivery = (By.XPATH, "//div[contains(@class,'radio')]//input[@value='2']")
        # locator_radio_no_delivery = (By.XPATH, "(//span[@class='radio__label'])[3]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.presence_of_element_located(locator_radio_no_delivery))

    # Поле Номер счета
    def get_title_invoice(self):
        locator_title = (By.XPATH, "//input[@name='title']")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_title))

    # Поле Адрес самовывоза
    def get_address_invoice(self):
        locator_address = (By.XPATH, "(//input[@name='delivery_address_id'])[1]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.presence_of_element_located(locator_address))

    # Поле предоплата
    def get_prepayment_invoice(self):
        locator_prepayment = (By.XPATH, "//input[@name='prepayment']")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_prepayment))

    # Поле отсрочка
    def get_payment_deferment_invoice(self):
        locator_payment_deferment = (By.XPATH, "//input[@name='payment_deferment']")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_payment_deferment))

    # Прикрепленный файл
    def get_title_file_invoice(self):
        locator_title_file = (By.XPATH, "//div[@class='tags-group']//div[contains(@class,'tag')][1]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_title_file))

    # Наименования позиций, товарные категории,кол-во, цена, единицы измерения -список
    def get_positions_invoice(self):
        locator_positions = (By.XPATH, "(//div[@class='h-full'])[2]//div[@class='truncate text-description']")
        self.driver.implicitly_wait(DataTest.implicitly_wait)
        return self.driver.find_elements(*locator_positions)

    # Methods

    # сортировка по столбцу Создана
    def sort_create(self):
        self.click_element(self.get_sort_create())

    # время и дата создания запроса
    def datetime_create(self):
        return self.get_datetime_first().text

# Окно создания счета

    # Наименования товарных позиций список
    def get_names_positions(self):
        card_info = []
        for i in range(0, len(self.get_positions()), 4):
            card_info.append(self.get_positions()[i].text.lower())
        return card_info

    def get_units_positions(self):
        card_info = []
        for i in range(2, len(self.get_positions()), 4):
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
            self.scroll_to_element(i)
            time.sleep(0.5)
            self.click_element(i)

    # Заполнить цены
    def input_price(self):
        price_info = []
        for i in self.get_price():
            # self.scroll_to_element(i)
            # time.sleep(0.5)
            # self.input_field(i, str(round(uniform(0.01, 9999999999.99), 2)))
            self.input_field(i, str(randint(1, 9999999999)))
            price_info.append(i.get_attribute('value'))
        return sorted(price_info)

# Окно Информации по запросу
    # Наименования товарных позиций список
    def get_names_positions_info(self):
        card_info = []
        for i in range(0, len(self.get_positions_info()), 4):
            card_info.append(self.get_positions_info()[i].text.lower())
        return card_info

    # Единицы измерения товарных позиций список
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

# Окно Посмотреть счет

    # Наименования товарных позиций список
    def get_names_positions_invoice(self):
        card_info = []
        for i in range(0, len(self.get_positions_invoice()), 6):
            card_info.append(self.get_positions_invoice()[i].text.lower())
        return card_info

    def get_units_positions_invoice(self):
        card_info = []
        for i in range(2, len(self.get_positions_invoice()), 6):
            card_info.append(self.get_positions_invoice()[i].text.lower())
        return card_info

    # Кол-во товаров по позициям
    def get_quantity_positions_invoice(self):
        card_info = []
        for i in range(3, len(self.get_positions_invoice()), 6):
            card_info.append(self.get_positions_invoice()[i].text)
        return sorted(card_info)

    # Цены товаров список
    def get_prices_positions_invoice(self):
        card_info = []
        for i in range(4, len(self.get_positions_invoice()), 6):
            card_info.append(self.get_positions_invoice()[i].text.lower())
        return sorted(card_info)

