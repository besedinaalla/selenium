import datetime
import os
import pathlib
import time
from pathlib import Path
import pyautogui
import pytest

from osmohub_auto.osmohub_work.pages.cart_page import CartPage
from osmohub_auto.osmohub_work.pages.catalog_page import CatalogPage
from osmohub_auto.osmohub_work.pages.enquiries_page import EnquiriesPage
from osmohub_auto.osmohub_work.pages.inquiries_buyer_page import InquiryBuyerPage
from osmohub_auto.osmohub_work.pages.inquiries_seller_page import InquirySellerPage
from osmohub_auto.osmohub_work.pages.login_page import LoginPage
from osmohub_auto.osmohub_work.pages.main_page import MainPage
from osmohub_auto.osmohub_work.tests.data_tests import DataTest


@pytest.mark.usefixtures("driver_init")
class TestCart:
    # Проверка товары из популярного в корзине
    def test_baskets(self):
        # экземпляры страниц
        catalog_page = CatalogPage(self.driver)
        cart_page = CartPage(self.driver)
        catalog_page.open_page()
        # обошли сертификат
        if self.driver.name == 'chrome':
            SslPage(self.driver).sert()
        # авторизовались, закрыли дебаг меню, приняли куки
        LoginPage(self.driver).authorization(login_correct_buyer, password_correct_buyer)
        MainPage(self.driver).close_debug()
        MainPage(self.driver).agree_cookie()
        # положили Популярное в корзину
        catalog_page.put_popular_product_in_cart()
        # составили списки наименований товаров из Популярного
        names_products_catalog = catalog_page.names_card_info()
        # print(names_products_catalog)
        # проверили кол-во добавленных товаров равно кол-ву в уведомлении в корзине
        catalog_page.assert_text(catalog_page.get_status_cart(), str(len(catalog_page.get_baskets())))
        print("Тест в корзину отправлено и в уведомлении 10 выбранных товаров")
        # перешли в корзину
        time.sleep(1)
        catalog_page.go_to_cart()
        # составили списки наименований товаров в корзине
        names_products_cart = cart_page.names_card_info()
        # print(names_products_cart)
        # проверили товары из популярного в корзине
        catalog_page.assert_items_of_list(names_products_catalog, names_products_cart)
        print("Тест в корзине находятся все 10 выбранных товаров пройден")
        # очистили корзину
        cart_page.clear_all_cart()
    #
    # # Проверка формирования заявки из каталога - самовывоз
    # def test_make_order_pickup(self):
    #     # экземпляры страниц
    #     catalog_page = CatalogPage(self.driver)
    #     cart_page = CartPage(self.driver)
    #     catalog_page.open_page()
    #     enquiries_page = EnquiriesPage(self.driver)
    #     # обошли сертификат
    #     if self.driver.name == 'chrome':
    #         SslPage(self.driver).sert()
    #     # авторизовались, закрыли дебаг меню, приняли куки
    #     LoginPage(self.driver).authorization(login_correct_buyer, password_correct_buyer)
    #     MainPage(self.driver).close_debug()
    #     MainPage(self.driver).agree_cookie()
    #     # положили Популярное в корзину перешли в корзину
    #     catalog_page.put_popular_product_in_cart()
    #     time.sleep(1)
    #     catalog_page.go_to_cart()
    #     # составили списки наименований товаров, кол-во позиций, кол-во товаров по позициям в корзине
    #     names_products_cart = cart_page.names_card_info()
    #     # print(names_products_cart)
    #     number_products_cart = len(names_products_cart)
    #     quantity_products_cart = cart_page.get_quantity_card_info()
    #     # print(quantity_products_cart)
    #     # сделали заказ, зафиксировали время заказа +- 5 сек
    #     cart_page.make_order()
    #     datetime_order = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    #     # print(datetime_order)
    #     datetime_order_minus5sec = (datetime.datetime.now() - datetime.timedelta(seconds=5)).strftime("%d.%m.%Y %H:%M")
    #     # print(datetime_order_minus5sec)
    #     datetime_order_plus5sec = (datetime.datetime.now() + datetime.timedelta(seconds=5)).strftime("%d.%m.%Y %H:%M")
    #     # print(datetime_order_plus5sec)
    #     # Перешли в заявки
    #     cart_page.go_to_enquiries()
    #     # отсортировали по дате создания
    #     enquiries_page.sort_create()
    #     enquiries_page.sort_create()
    #     time.sleep(2)
    #     # проверили дату и время заявки
    #     enquiries_page.assert_time_in_range(enquiries_page.get_date_last(), enquiries_page.get_time_last(), datetime_order_minus5sec, datetime_order_plus5sec)
    #     print("Тест: Новая заявка в списке заявок")
    #     # проверили кол-во позиций в зявке с корзиной
    #     enquiries_page.assert_text(enquiries_page.get_number_positions(), str(number_products_cart))
    #     print("Тест: В заявке 10 товарных позиций")
    #     # проверили статус заявки
    #     enquiries_page.assert_text(enquiries_page.get_enquiry_status(), 'новая')
    #     print("Тест: Статус заявки новая")
    #     # перешели в информацию по заявке
    #     enquiries_page.click_element(enquiries_page.get_vertical_dots())
    #     enquiries_page.click_element(enquiries_page.get_information())
    #     # составили списки наименований товаров, кол-во товаров по позициям в корзине
    #     names_products_enquiry = enquiries_page.get_names_positions()
    #     # print(names_products_enquiry)
    #     quantity_products_enquiry = enquiries_page.get_quantity_positions()
    #     # print(quantity_products_enquiry)
    #     # проверили наименования товарных позиций в заявке
    #     enquiries_page.assert_items_of_list(names_products_enquiry, names_products_cart)
    #     print("Тест: Товары в заявке = товарам в корзине (наименования)")
    #     # проверили кол-во товаров по позициям
    #     enquiries_page.assert_lists(quantity_products_enquiry, quantity_products_cart)
    #     print("Тест: Товары в заявке = товарам в корзине (кол-во)")

    # # Проверка формирования заявки из каталога - доставка по старому адрресу
    # def test_make_order_delivery_old_address(self):
    #     # экземпляры страниц
    #     catalog_page = CatalogPage(self.driver)
    #     cart_page = CartPage(self.driver)
    #     catalog_page.open_page()
    #     enquiries_page = EnquiriesPage(self.driver)
    #     # обошли сертификат
    #     if self.driver.name == 'chrome':
    #         SslPage(self.driver).sert()
    #     # авторизовались, закрыли дебаг меню, приняли куки
    #     LoginPage(self.driver).authorization(login_correct_buyer, password_correct_buyer)
    #     MainPage(self.driver).close_debug()
    #     MainPage(self.driver).agree_cookie()
    #     # положили Популярное в корзину перешли в корзину
    #     catalog_page.put_popular_product_in_cart()
    #     time.sleep(1)
    #     catalog_page.go_to_cart()
    #     # составили списки наименований товаров, кол-во позиций, кол-во товаров по позициям в корзине
    #     names_products_cart = cart_page.names_card_info()
    #     # print(names_products_cart)
    #     number_products_cart = len(names_products_cart)
    #     quantity_products_cart = cart_page.get_quantity_card_info()
    #     # print(quantity_products_cart)
    #     # перешли во вкладку Доставка и выбрали адрес
    #     cart_page.delivery_address_old()
    #     # записали адрес доставки
    #     delivery_address = cart_page.get_delivery_address().text
    #     # выбрали адрес
    #     cart_page.click_element(cart_page.get_choose_address())
    #     # Проверили адрес, отобразился в корзине
    #     cart_page.assert_text(cart_page.get_cart_delivery_after_choose(), delivery_address)
    #     print("Тест: Выбранный адрес в корзине")
    #     # сделали заказ, зафиксировали время заказа +- 5 сек
    #     cart_page.make_order()
    #     datetime_order = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    #     # print(datetime_order)
    #     datetime_order_minus5sec = (datetime.datetime.now() - datetime.timedelta(seconds=5)).strftime("%d.%m.%Y %H:%M")
    #     # print(datetime_order_minus5sec)
    #     datetime_order_plus5sec = (datetime.datetime.now() + datetime.timedelta(seconds=5)).strftime("%d.%m.%Y %H:%M")
    #     # print(datetime_order_plus5sec)
    #     # Перешли в заявки
    #     cart_page.go_to_enquiries()
    #     # отсортировали по дате создания
    #     enquiries_page.sort_create()
    #     enquiries_page.sort_create()
    #     time.sleep(2)
    #     # проверили дату и время заявки
    #     enquiries_page.assert_time_in_range(enquiries_page.get_date_last(), enquiries_page.get_time_last(), datetime_order_minus5sec, datetime_order_plus5sec)
    #     print("Тест: Новая заявка в списке заявок")
    #     # проверили кол-во позиций в зявке с корзиной
    #     enquiries_page.assert_text(enquiries_page.get_number_positions(), str(number_products_cart))
    #     print("Тест: В заявке 10 товарных позиций")
    #     # проверили статус заявки
    #     enquiries_page.assert_text(enquiries_page.get_enquiry_status(), 'новая')
    #     print("Тест: Статус заявки новая")
    #     # перешели в информацию по заявке
    #     enquiries_page.click_element(enquiries_page.get_vertical_dots())
    #     enquiries_page.click_element(enquiries_page.get_information())
    #     # составили списки наименований товаров, кол-во товаров по позициям в корзине
    #     names_products_enquiry = enquiries_page.get_names_positions()
    #     # print(names_products_enquiry)
    #     quantity_products_enquiry = enquiries_page.get_quantity_positions()
    #     # print(quantity_products_enquiry)
    #     # проверили наименования товарных позиций в заявке
    #     enquiries_page.assert_items_of_list(names_products_enquiry, names_products_cart)
    #     print("Тест: Товары в заявке = товарам в корзине (наименования)")
    #     # проверили кол-во товаров по позициям
    #     enquiries_page.assert_lists(quantity_products_enquiry, quantity_products_cart)
    #     print("Тест: Товары в заявке = товарам в корзине (кол-во)")

    #
    # # Проверка формирования заявки из каталога - доставка по новому адрресу
    # def test_make_order_delivery_new_address(self):
    #     # экземпляры страниц
    #     catalog_page = CatalogPage(self.driver)
    #     cart_page = CartPage(self.driver)
    #     catalog_page.open_page()
    #     enquiries_page = EnquiriesPage(self.driver)
    #     # обошли сертификат
    #     if self.driver.name == 'chrome':
    #         SslPage(self.driver).sert()
    #     # авторизовались, закрыли дебаг меню, приняли куки
    #     LoginPage(self.driver).authorization(login_correct_buyer, password_correct_buyer)
    #     MainPage(self.driver).close_debug()
    #     MainPage(self.driver).agree_cookie()
    #     # положили Популярное в корзину перешли в корзину
    #     catalog_page.put_popular_product_in_cart()
    #     time.sleep(1)
    #     catalog_page.go_to_cart()
    #     # составили списки наименований товаров, кол-во позиций, кол-во товаров по позициям в корзине
    #     names_products_cart = cart_page.names_card_info()
    #     # print(names_products_cart)
    #     number_products_cart = len(names_products_cart)
    #     quantity_products_cart = cart_page.get_quantity_card_info()
    #     # print(quantity_products_cart)
    #     # перешли во вкладку Доставка и выбрали адрес
    #     cart_page.delivery_address_new()
    #     # записали адрес доставки
    #     delivery_address = cart_page.get_delivery_address_last().text
    #     # выбрали адрес
    #     cart_page.click_element(cart_page.get_choose_address())
    #     # Проверили адрес, отобразился в корзине
    #     cart_page.assert_text(cart_page.get_cart_delivery_after_choose(), delivery_address)
    #     print("Тест: Выбранный адрес в корзине")
    #     # сделали заказ, зафиксировали время заказа +- 5 сек
    #     cart_page.make_order()
    #     datetime_order = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    #     # print(datetime_order)
    #     datetime_order_minus5sec = (datetime.datetime.now() - datetime.timedelta(seconds=5)).strftime("%d.%m.%Y %H:%M")
    #     # print(datetime_order_minus5sec)
    #     datetime_order_plus5sec = (datetime.datetime.now() + datetime.timedelta(seconds=5)).strftime("%d.%m.%Y %H:%M")
    #     # print(datetime_order_plus5sec)
    #     # Перешли в заявки
    #     cart_page.go_to_enquiries()
    #     # отсортировали по дате создания
    #     enquiries_page.sort_create()
    #     enquiries_page.sort_create()
    #     time.sleep(2)
    #     # проверили дату и время заявки
    #     enquiries_page.assert_time_in_range(enquiries_page.get_date_last(), enquiries_page.get_time_last(), datetime_order_minus5sec, datetime_order_plus5sec)
    #     print("Тест: Новая заявка в списке заявок")
    #     # проверили кол-во позиций в зявке с корзиной
    #     enquiries_page.assert_text(enquiries_page.get_number_positions(), str(number_products_cart))
    #     print("Тест: В заявке 10 товарных позиций")
    #     # проверили статус заявки
    #     enquiries_page.assert_text(enquiries_page.get_enquiry_status(), 'новая')
    #     print("Тест: Статус заявки новая")
    #     # перешели в информацию по заявке
    #     enquiries_page.click_element(enquiries_page.get_vertical_dots())
    #     enquiries_page.click_element(enquiries_page.get_information())
    #     # составили списки наименований товаров, кол-во товаров по позициям в корзине
    #     names_products_enquiry = enquiries_page.get_names_positions()
    #     # print(names_products_enquiry)
    #     quantity_products_enquiry = enquiries_page.get_quantity_positions()
    #     # print(quantity_products_enquiry)
    #     # проверили наименования товарных позиций в заявке
    #     enquiries_page.assert_items_of_list(names_products_enquiry, names_products_cart)
    #     print("Тест: Товары в заявке = товарам в корзине (наименования)")
    #     # проверили кол-во товаров по позициям
    #     enquiries_page.assert_lists(quantity_products_enquiry, quantity_products_cart)
    #     print("Тест: Товары в заявке = товарам в корзине (кол-во)")









        # Проверка заявки не из каталога- заполнение вручную

        # Проверка заявки не из каталога- загрузка шаблона
