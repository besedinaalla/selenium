import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from osmohub_auto.osmohub_work.base.base_page import BasePage

# Класс страницы каталога
from osmohub_auto.osmohub_work.pages.cart_page import CartPage
from osmohub_auto.osmohub_work.tests.data_tests import DataTest


class CatalogPage(BasePage):


    def __init__(self, driver, url=DataTest.url+'/catalog'):
        super().__init__(driver, url)
        self.driver = driver

    # Getters # Locators Локаторы элементов и получение этих элементов

    # Иконка корзинка у товара- список
    def get_baskets(self):
        locator_baskets = (By.XPATH, "//button[contains(@class,'category-card__buttons__basket')]")
        self.driver.implicitly_wait(DataTest.implicitly_wait)
        return self.driver.find_elements(*locator_baskets)

    # Иконка корзинка у последнего товара
    def get_last_basket(self):
        locator_last_basket = (By.XPATH, "(//button[contains(@class,'category-card__buttons__basket')])[10]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_last_basket))

    # Иконка корзина
    def get_cart(self):
        locator_cart = (By.XPATH, "//a[@class ='catalog-link cart-status-link']")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_cart))

    # Иконка количество товаров в корзине
    def get_status_cart(self):
        locator_status_cart = (By.XPATH, "//div[contains(@class,'cart-status-badge')]")
        return WebDriverWait(self.driver, DataTest.wait).until(EC.element_to_be_clickable(locator_status_cart))

    # Иконка количество товаров в корзине-список
    def get_status_cart_list(self):
        locator_status_cart = (By.XPATH, "//div[contains(@class,'cart-status-badge')]")
        self.driver.implicitly_wait(DataTest.implicitly_wait)
        return self.driver.find_elements(*locator_status_cart)

    # Локатор Наименования товаров
    def get_names_popular_products(self):
        locator_names_popular_products = (By.XPATH, "//div[@class='category-card__info']/a[contains(@href,'product')]")
        return self.driver.find_elements(*locator_names_popular_products)

    # метод получить наименования товаров
    def names_popular_products(self):
        card_info = []
        for i in self.get_names_popular_products():
            card_info.append(i.text.lower())
        return card_info

    # Метод проверить корзину, очистить ее при необходимости и вернуться в каталог
    def check_and_clear_cart(self):
        if len(self.get_status_cart_list()) > 0:
            self.go_to_cart()
            time.sleep(2)
            CartPage(self.driver).clear_all_cart()
            time.sleep(2)
            CartPage(self.driver).go_to_catalog()

    # Метод положить все товары из Популярного в корзину
    def put_popular_product_in_cart(self):
        self.check_and_clear_cart()
        time.sleep(2)
        for i in self.get_baskets():
            self.scroll_to_element(i)
            time.sleep(0.5)
            self.click_element(i)

    # Метод перейти в корзину со страницы каталога
    def go_to_cart(self):
        self.click_element(self.get_cart())
