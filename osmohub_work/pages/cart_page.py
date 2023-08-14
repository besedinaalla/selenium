import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from osmohub_auto.osmohub_work.base.base_page import BasePage


# Класс страницы корзины
from osmohub_auto.osmohub_work.tests.data_tests import DataTest


class CartPage(BasePage):

    def __init__(self, driver, url=DataTest.url+'/cart'):
        super().__init__(driver, url)
        self.driver = driver

    # Getters # Locators Локаторы элементов и получение этих элементов

    # Каталог
    def get_catalog(self):
        locator_catalog = (By.XPATH, "//a[text()='Каталог']")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_catalog))

    # Иконка количество товаров в корзине
    def get_status_cart(self):
        locator_status_cart = (By.XPATH, "//a[@class ='catalog-link cart-status-link']")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_status_cart))

    # Наименования товаров в корзине (список)
    def get_card_info(self):
        locator_card_info = (By.XPATH, "//div[@class='category-card__info']/a[contains(@href,'product')]")
        self.driver.implicitly_wait(DataTest.implicitly_wait)
        return self.driver.find_elements(*locator_card_info)

    # Наименование последнего товара
    def get_last_product(self):
        locator_last_product = (By.XPATH, "(//div[@class='category-card__info']/a[contains(@href,'product')])[10]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_last_product))

    # Кол-во товаров в корзине (список)
    def get_quantity_cart(self):
        locator_quantity_cart = (By.XPATH, "//input[@class='quantity-plus-minus__input']")
        self.driver.implicitly_wait(DataTest.implicitly_wait)
        return self.driver.find_elements(*locator_quantity_cart)

    # Кнопка Удалить все
    def get_delete_all(self):
        locator_delete_all = (By.XPATH, "//div[@class='cart-list__delete-all-btn']/button")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_delete_all))

    # Кнопка Сделать заказ
    def get_submit_order(self):
        locator_submit_order = (By.XPATH, "//button[contains(@class,'cart__btn-submit')]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_submit_order))

    # Вкладка Доставка
    def get_delivery(self):
        locator_get_delivery = (By.XPATH, "//button[text()='Доставка']")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_get_delivery))

    # Укажите адрес доставки
    def get_cart_delivery(self):
        locator_get_cart_delivery = (By.XPATH, "//div[@name='delivery']/h5")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_get_cart_delivery))

    # Курьерской доставкой по адресу
    def get_cart_delivery_after_choose(self):
        locator_get_cart_delivery_after = (By.XPATH, "//div[@name='delivery']/span[contains(@class,'cart-delivery-description')]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_get_cart_delivery_after))

    # Поле ввода адреса
    def get_input_address(self):
        locator_get_input_address = (By.XPATH, "//input[@name='address']")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_get_input_address))

    # Выпадающий список
    def get_dropdown_address(self):
        locator_get_dropdown_address = (By.XPATH, "//div[contains(@class,'add-delivery-address')]//div[@class='elevation-1 typeahead-depr__dropdown']")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_get_dropdown_address))

    # Адрес из выпадающего списка
    def get_address_from_dropdown(self):
        locator_get_address_from_dropdown_ = (By.XPATH, "//div[contains(@class,'dropdown__option')][1]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_get_address_from_dropdown_))

    # Кнопка Добавить новый
    def get_add_address(self):
        locator_get_add_address = (By.XPATH, "//button[text()='Добавить новый']")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_get_add_address))

    # Кнопка Выбрать
    def get_choose_address(self):
        locator_get_choose_address = (By.XPATH, "//button[text()='Выбрать']")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_get_choose_address))

    # Конкретный адрес первый
    def get_delivery_address(self):
        locator_get_delivery_address = (By.XPATH, "//div[@class='delivery-address-main']/div[contains(@class,'delivery-address ')][1]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_get_delivery_address))

    # Конкретный адрес последний
    def get_delivery_address_last(self):
        locator_get_delivery_address = (By.XPATH, "//div[@class='delivery-address-main']/div[contains(@class,'delivery-address ')][last()]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_get_delivery_address))

    # Кнопка Перейти в заявки
    def get_go_to_enquiries(self):
        # locator_go_to_enquiries = (By.XPATH, "//a[text()='Перейти в заявки']")
        locator_go_to_enquiries = (By.XPATH, "//a[text()='Заявки']")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_go_to_enquiries))

    # Метод

    # Метод перейти в каталог со страницы корзины
    def go_to_catalog(self):
        self.click_element(self.get_catalog())

    # Получить наименования товаров в корзине
    def names_card_info(self):
        card_info = []
        for i in self.get_card_info():
            card_info.append(i.text.lower())
        return card_info

    # Получить кол-во каждого товара в корзине
    def get_quantity_card_info(self):
        card_info = []
        for i in self.get_quantity_cart():
            card_info.append(i.get_attribute("value"))
        return sorted(card_info)

    # Очистить корзину
    def clear_all_cart(self):
        self.click_element(self.get_delete_all())

    # Сделать заказ
    def make_order(self):
        self.click_element(self.get_submit_order())

    # Перейти в заявки
    def go_to_enquiries(self):
        self.click_element(self.get_go_to_enquiries())

    # Выбор адреса доставки
    def delivery_address_new(self):
        self.click_element(self.get_delivery())
        self.click_element(self.get_cart_delivery())
        self.input_field(self.get_input_address(), 'Мурманск')
        time.sleep(2)
        new_address = self.get_address_from_dropdown().text
        self.click_element(self.get_address_from_dropdown())
        print(new_address)
        self.click_element(self.get_add_address())
        time.sleep(2)
        self.click_element(self.get_delivery_address_last())
        self.assert_text(self.get_delivery_address_last(), new_address)
        print("Тест: Выбранный адрес добавлен в список адресов")

        # delivery_address = self.get_delivery_address().text
        # self.click_element(self.get_choose_address())

    # Выбор адреса доставки существующего
    def delivery_address_old(self):
        self.click_element(self.get_delivery())
        self.click_element(self.get_cart_delivery())
        self.click_element(self.get_delivery_address())



        # delivery_address = self.get_delivery_address().text
        # self.click_element(self.get_choose_address())
