import datetime
import pathlib
import time
from pathlib import Path
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
class TestOrderCatalog:
    # Проверка формирования заявки из каталога - самовывоз
    # def test_make_order_catalog(self):
    #     # экземпляры страниц
    #     main_page = MainPage(self.driver)
    #     login_page = LoginPage(self.driver)
    #     catalog_page = CatalogPage(self.driver)
    #     cart_page = CartPage(self.driver)
    #     enquiries_page = EnquiriesPage(self.driver)
    #     inquiry_buyer_page = InquiryBuyerPage(self.driver)
    #
    #     main_page.open_page_ssl_debug()
    #     # # Открыли главную страницу
    #     # main_page.open_page()
    #     #
    #     # # обошли сертификат сделать в методе на гл странице в опен пейдж без ссл
    #     # if self.driver.name == 'chrome':
    #     #     SslPage(self.driver).sert()
    #
    #     # нажали Войти на главной странице
    #     main_page.click_element(main_page.get_login())
    #
    #     # авторизовались, приняли куки
    #     login_page.authorization(login_correct_buyer, password_correct_buyer)
    #     # main_page.close_debug()
    #     main_page.agree_cookie()
    #
    #     # положили Популярное в корзину перешли в корзину
    #     catalog_page.put_popular_product_in_cart()
    #
    #     # составили списки наименований товаров из Популярного
    #     names_products_catalog = catalog_page.names_card_info()
    #     # print(names_products_catalog)
    #
    #     # проверили кол-во добавленных товаров равно кол-ву в уведомлении в корзине
    #     catalog_page.assert_text(catalog_page.get_status_cart(), str(len(catalog_page.get_baskets())))
    #     print("Тест в корзину отправлено и в уведомлении 10 выбранных товаров")
    #
    #     # перешли в корзину
    #     time.sleep(1)
    #     catalog_page.go_to_cart()
    #
    #     # составили списки наименований товаров, кол-во позиций, кол-во товаров по позициям в корзине
    #     names_products_cart = cart_page.names_card_info()
    #     # print(names_products_cart)
    #     number_products_cart = len(names_products_cart)
    #     quantity_products_cart = cart_page.get_quantity_card_info()
    #     # print(quantity_products_cart)
    #
    #     # проверили товары из популярного в корзине
    #     catalog_page.assert_items_of_list(names_products_catalog, names_products_cart)
    #     print("Тест в корзине находятся все 10 выбранных товаров")
    #
    #     # сделали заказ, зафиксировали время заказа +- 5 сек
    #     cart_page.make_order()
    #     datetime_order = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    #     # print(datetime_order)
    #     datetime_order_minus5sec = (datetime.datetime.now() - datetime.timedelta(seconds=5)).strftime("%d.%m.%Y %H:%M")
    #     # print(datetime_order_minus5sec)
    #     datetime_order_plus5sec = (datetime.datetime.now() + datetime.timedelta(seconds=5)).strftime("%d.%m.%Y %H:%M")
    #     # print(datetime_order_plus5sec)
    #
    #     # Перешли в заявки
    #     cart_page.go_to_enquiries()
    #     # отсортировали по дате создания
    #     enquiries_page.sort_create()
    #     enquiries_page.sort_create()
    #     time.sleep(2)
    #
    #     # проверили дату и время заявки
    #     enquiries_page.assert_time_in_range(enquiries_page.datetime_create(), datetime_order_minus5sec, datetime_order_plus5sec)
    #     print("Тест: Новая заявка в списке заявок")
    #
    #     # проверили кол-во позиций в зявке с корзиной
    #     enquiries_page.assert_text(enquiries_page.get_number_positions(), str(number_products_cart))
    #     print("Тест: В заявке 10 товарных позиций")
    #
    #     # проверили статус заявки
    #     enquiries_page.assert_text(enquiries_page.get_enquiry_status(), 'новая')
    #     print("Тест: Статус заявки новая")
    #
    #     # перешели в информацию по заявке
    #     enquiries_page.click_element(enquiries_page.get_vertical_dots())
    #     enquiries_page.click_element(enquiries_page.get_information())
    #
    #     # составили списки наименований товаров, кол-во товаров по позициям в заявке
    #     names_products_enquiry = enquiries_page.get_names_positions()
    #     # print(names_products_enquiry)
    #     quantity_products_enquiry = enquiries_page.get_quantity_positions()
    #     # print(quantity_products_enquiry)
    #
    #     # проверили наименования товарных позиций в заявке
    #     enquiries_page.assert_items_of_list(names_products_enquiry, names_products_cart)
    #     print("Тест: Товары в заявке = товарам в корзине (наименования)")
    #
    #     # проверили кол-во товаров по позициям
    #     enquiries_page.assert_lists(quantity_products_enquiry, quantity_products_cart)
    #     print("Тест: Товары в заявке = товарам в корзине (кол-во)")
    #
    #     # Вышли из информации по заявке
    #     enquiries_page.click_element(enquiries_page.get_exit_information())
    #
    #     # Выбрали первую заявку
    #     enquiries_page.click_element(enquiries_page.get_checkbox_enquiry())
    #
    #     # Нажали отправить запрос
    #     enquiries_page.click_element(enquiries_page.get_send_request())
    #
    #     # Проверили поле Требуется доставка
    #     inquiry_buyer_page.assert_value_attribute(inquiry_buyer_page.get_yes_no_delivery(), 'value', 'нет')
    #     print("Тест: Выбран самовывоз")
    #
    #     # Составили списки наименований товаров, кол-во товаров по позициям в запросе
    #     names_products_inquiry = inquiry_buyer_page.get_names_positions()
    #     # print(names_products_inquiry)
    #     quantity_products_inquiry = inquiry_buyer_page.get_quantity_positions()
    #     # print(quantity_products_inquiry)
    #
    #     # Проверили наименование товарных позиций и их кол-во
    #     inquiry_buyer_page.assert_items_of_list(names_products_inquiry, names_products_enquiry)
    #     print("Тест: Товары в запросе = товарам в заявке (наименование)")
    #
    #     # Проверили кол-во товарных позиций
    #     inquiry_buyer_page.assert_lists(quantity_products_inquiry, quantity_products_enquiry)
    #     print("Тест: Товары в запросе = товарам в заявке (кол-во)")
    #
    #     # Заполнили поля Грузополучатель, Комментарий,Отсрочка
    #     inquiry_buyer_page.input_field(inquiry_buyer_page.get_recipient(), 'Петров П.П.')
    #     inquiry_buyer_page.input_field(inquiry_buyer_page.get_delay_payment(), '10')
    #     inquiry_buyer_page.input_field(inquiry_buyer_page.get_comment(), 'срочно')
    #
    #     # Выбрали поставщика, записали его имя
    #     inquiry_buyer_page.click_element(inquiry_buyer_page.get_seller())
    #     inquiry_buyer_page.click_element(inquiry_buyer_page.get_checkbox_seller())
    #     name_seller = inquiry_buyer_page.get_name_seller().text
    #     # print(name_seller)
    #
    #     # Проверили, что в поле выбранный поставщик
    #     inquiry_buyer_page.assert_text(inquiry_buyer_page.get_name_choose_seller(), name_seller)
    #     print("Тест: Выбранный поставщик в поле Поставщик")
    #
    #     # Выбрали позиции
    #     inquiry_buyer_page.check_all_positions()
    #
    #     # Нажали Послать запрос
    #     inquiry_buyer_page.click_element(inquiry_buyer_page.get_send_request())
    #     time.sleep(5)
    #     # Зафиксировали время отправки запроса
    #     datetime_request = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    #     # print(datetime_order)
    #     datetime_request_minus5sec = (datetime.datetime.now() - datetime.timedelta(seconds=5)).strftime("%d.%m.%Y %H:%M")
    #     # print(datetime_request_minus5sec)
    #     datetime_request_plus5sec = (datetime.datetime.now() + datetime.timedelta(seconds=5)).strftime("%d.%m.%Y %H:%M")
    #     # print(datetime_request_plus5sec)
    #
    #     # проверили статус заявки
    #     enquiries_page.assert_text(enquiries_page.get_enquiry_status(), 'в работе')
    #     print("Тест: Статус заявки в работе")
    #
    #     # перешели в информацию по заявке во вкладку Запросы
    #     enquiries_page.tab_inquiries()
    #
    #     # проверили поставщика, размещено, статус
    #     inquiry_buyer_page.assert_text(inquiry_buyer_page.get_seller_inquiry(), name_seller)
    #     print("Тест: Поставщик в запросе отображается верно")
    #     inquiry_buyer_page.assert_time_in_range(inquiry_buyer_page.datetime_create(), datetime_request_minus5sec, datetime_request_plus5sec)
    #     print("Тест: Время размещения запроса отображается верно")
    #     inquiry_buyer_page.assert_text(inquiry_buyer_page.get_status_inquiry(), 'ожидает')
    #     print("Тест: Статус запроса ожидает")
    #
    #     # зашли в информацию
    #     inquiry_buyer_page.click_element(inquiry_buyer_page.get_vertical_dots())
    #     inquiry_buyer_page.click_element(inquiry_buyer_page.get_information())
    #
    #     # проверили поля
    #     inquiry_buyer_page.assert_value_attribute(inquiry_buyer_page.get_recipient_info(), 'value', 'Петров П.П.')
    #     inquiry_buyer_page.assert_value_attribute(inquiry_buyer_page.get_yes_no_delivery_info(), 'value', 'нет')
    #     inquiry_buyer_page.assert_value_attribute(inquiry_buyer_page.get_delay_payment_info(), 'value', '10')
    #     print("Тест: Поля заполнены в соотвествии с запросом")
    #
    #     # проверили позиции
    #     inquiry_buyer_page.assert_items_of_list(inquiry_buyer_page.get_names_positions_info(), names_products_inquiry)
    #     print("Тест: Товары в отправленном запросе = товарам в информации о запросе")
    #
    #     # проверили кол-во
    #     inquiry_buyer_page.assert_lists(inquiry_buyer_page.get_quantity_positions_info(), quantity_products_inquiry)
    #     print("Тест: Кол-во товаров в отправленном запросе = кол-ву товаров в информации о запросе")

    def test_order_catalog_pickup(self):
        # экземпляры страниц
        main_page = MainPage(self.driver)
        login_page = LoginPage(self.driver)
        catalog_page = CatalogPage(self.driver)
        cart_page = CartPage(self.driver)
        enquiries_page = EnquiriesPage(self.driver)
        inquiry_buyer_page = InquiryBuyerPage(self.driver)
        inquiry_seller_page = InquirySellerPage(self.driver)

        # Открыли главную страницу, обошли сертификат и дебаг
        main_page.open_page_ssl_debug()

        # приняли куки
        main_page.agree_cookie()

        # нажали Войти на главной странице
        main_page.click_element(main_page.get_login())

        print("================ПОКУПАТЕЛЬ================")

        # авторизовались
        login_page.authorization(DataTest.login_correct_buyer, DataTest.password_correct_buyer)

        print("================Проверка корзины================")

        # положили Популярное в корзину
        catalog_page.put_popular_product_in_cart()

        # составили списки наименований товаров из Популярного
        names_products_catalog = catalog_page.names_popular_products()

        # проверили кол-во добавленных товаров равно кол-ву в уведомлении в корзине
        catalog_page.assert_text(catalog_page.get_status_cart(), str(len(catalog_page.get_baskets())))
        print("Тест в корзину отправлено и в уведомлении 10 товаров")

        # перешли в корзину
        time.sleep(1)
        catalog_page.go_to_cart()

        # составили списки наименований товаров, кол-во позиций, кол-во товаров по позициям в корзине
        time.sleep(2)
        names_products_cart = cart_page.names_card_info()
        print(names_products_cart)
        number_products_cart = len(names_products_cart)
        quantity_products_cart = cart_page.get_quantity_card_info()

        # проверили товары из популярного в корзине
        catalog_page.assert_items_of_list(names_products_catalog, names_products_cart)
        print("Тест в корзине находятся все товары из популярного")

        # сделали заказ, зафиксировали время заказа +- 5 сек
        cart_page.make_order()
        # datetime_order = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
        datetime_order_minus5sec = (datetime.datetime.now() - datetime.timedelta(seconds=5)).strftime("%d.%m.%Y %H:%M")
        datetime_order_plus5sec = (datetime.datetime.now() + datetime.timedelta(seconds=5)).strftime("%d.%m.%Y %H:%M")

        print("================Проверка заявки================")

        # Перешли в заявки
        cart_page.go_to_enquiries()

        # отсортировали по дате создания
        enquiries_page.sort_create()
        enquiries_page.sort_create()
        time.sleep(2)

        # проверили дату и время заявки
        enquiries_page.assert_time_in_range(enquiries_page.datetime_create(), datetime_order_minus5sec,
                                            datetime_order_plus5sec)
        print("Тест: Новая заявка в списке заявок. Дата и время ок")

        # проверили кол-во позиций в заявке
        enquiries_page.assert_text(enquiries_page.get_number_positions_first(), str(number_products_cart))
        print("Тест: В заявке 10 товарных позиций, как и в корзине")

        # проверили статус заявки
        enquiries_page.assert_text(enquiries_page.get_enquiry_status_first(), 'новая')
        print("Тест: Статус заявки новая")

        # записали имя заявки
        title_first_enquiry = enquiries_page.get_title_first().text

        # перешли в информацию по заявке
        enquiries_page.click_element(enquiries_page.get_vertical_dots())
        enquiries_page.click_element(enquiries_page.get_information())

        # составили списки наименований товаров, кол-во товаров по позициям в заявке
        names_products_enquiry = enquiries_page.get_names_positions()
        quantity_products_enquiry = enquiries_page.get_quantity_positions()

        # проверили наименования товарных позиций в заявке
        enquiries_page.assert_items_of_list(names_products_enquiry, names_products_cart)
        print("Тест: Товары в заявке = товарам в корзине (наименования)")

        # проверили кол-во товаров по позициям
        enquiries_page.assert_lists(quantity_products_enquiry, quantity_products_cart)
        print("Тест: Товары в заявке = товарам в корзине (кол-во)")

        # Вышли из информации по заявке
        enquiries_page.click_element(enquiries_page.get_exit_information())

        print("================Проверка окна формирования запроса================")

        # Выбрали первую заявку
        enquiries_page.click_element(enquiries_page.get_checkbox_enquiry_first())

        # Нажали отправить запрос
        enquiries_page.click_element(enquiries_page.get_send_inquiry())

        # Проверили поле Требуется доставка
        inquiry_buyer_page.assert_value_attribute(inquiry_buyer_page.get_yes_no_delivery(), 'value', 'нет')
        print("Тест: Выбран самовывоз")

        # Составили списки наименований товаров, кол-во товаров, единиц измерений по позициям в запросе
        names_products_inquiry = inquiry_buyer_page.get_names_positions()
        quantity_products_inquiry = inquiry_buyer_page.get_quantity_positions()
        units_inquiry = inquiry_buyer_page.get_units_positions()

        # Проверили наименование товарных позиций
        inquiry_buyer_page.assert_items_of_list(names_products_inquiry, names_products_enquiry)
        print("Тест: Товары в запросе = товарам в заявке (наименование)")

        # Проверили кол-во товарных позиций
        inquiry_buyer_page.assert_lists(quantity_products_inquiry, quantity_products_enquiry)
        print("Тест: Товары в запросе = товарам в заявке (кол-во)")

        # Заполнили поля Грузополучатель, Комментарий,Отсрочка
        inquiry_buyer_page.input_field(inquiry_buyer_page.get_recipient(), 'Петров П.П.')
        inquiry_buyer_page.input_field(inquiry_buyer_page.get_delay_payment(), '10')
        inquiry_buyer_page.input_field(inquiry_buyer_page.get_comment(), 'срочно')

        # Выбрали поставщика, записали его имя
        inquiry_buyer_page.click_element(inquiry_buyer_page.get_seller())
        inquiry_buyer_page.click_element(inquiry_buyer_page.get_checkbox_polyplastic())
        name_seller = 'ГРУППА ПОЛИПЛАСТИК'

        # Проверили, что в поле выбранный поставщик
        inquiry_buyer_page.assert_text(inquiry_buyer_page.get_name_choose_seller(), name_seller)
        print("Тест: Выбранный поставщик в поле Поставщик (полипластик)")

        # Выбрали все позиции
        inquiry_buyer_page.check_all_positions()

        # Нажали Послать запрос
        inquiry_buyer_page.click_element(inquiry_buyer_page.get_send_inquiry())

        # Зафиксировали время отправки запроса
        datetime_request_minus5sec = (datetime.datetime.now() - datetime.timedelta(seconds=5)).strftime("%d.%m.%Y %H:%M")
        datetime_request_plus5sec = (datetime.datetime.now() + datetime.timedelta(seconds=5)).strftime("%d.%m.%Y %H:%M")
        time.sleep(5)

        print("================Проверка изменения статуса заявки================")

        # проверили статус заявки
        enquiries_page.assert_text(enquiries_page.get_enquiry_status_first(), 'в работе')
        print("Тест: Статус заявки в работе")

        print("================Проверка вкладки Запросы================")

        # перешели в информацию по заявке во вкладку Запросы
        enquiries_page.tab_inquiries()

        # проверили наименование, поставщика, размещено, статус, покупателя
        inquiry_buyer_page.assert_text(inquiry_buyer_page.get_title_inquiry(), title_first_enquiry)
        print("Тест: Наименование запроса отображается верно")
        inquiry_buyer_page.assert_text(inquiry_buyer_page.get_buyer_inquiry(), 'ССР')
        print("Тест: создатель- Покупатель в запросе отображается верно")
        inquiry_buyer_page.assert_text(inquiry_buyer_page.get_seller_inquiry(), name_seller)
        print("Тест: исполнитель- Поставщик в запросе отображается верно")
        inquiry_buyer_page.assert_time_in_range(inquiry_buyer_page.datetime_create(), datetime_request_minus5sec,
                                                datetime_request_plus5sec)
        print("Тест: Время размещения запроса отображается верно")
        inquiry_buyer_page.assert_text(inquiry_buyer_page.get_status_inquiry(), 'ожидает')
        print("Тест: Статус запроса ожидает")

        print("================Проверка Запроса================")

        # зашли в информацию
        inquiry_buyer_page.tab_info()

        # проверили поля
        inquiry_buyer_page.assert_value_attribute(inquiry_buyer_page.get_buyer_info(), 'value', 'ССР/ИНН 7729790409')
        print("Тест: Покупатель в запросе отображается верно")
        inquiry_buyer_page.assert_value_attribute(inquiry_buyer_page.get_recipient_info(), 'value', 'Петров П.П.')
        print("Тест: Грузополучатель в запросе отображается верно")
        inquiry_buyer_page.assert_value_attribute(inquiry_buyer_page.get_yes_no_delivery_info(), 'value', 'нет')
        inquiry_buyer_page.assert_value_attribute(inquiry_buyer_page.get_address_info(), 'value', '-')
        print("Тест: Выбран самовывоз")
        inquiry_buyer_page.assert_value_attribute(inquiry_buyer_page.get_delay_payment_info(), 'value', '10')
        print("Тест: Отсрочка в запросе отображается верно")
        inquiry_buyer_page.assert_value_attribute(inquiry_buyer_page.get_seller_info(), 'value', '-')
        print("Тест: Поставщик в запросе отображается верно")
        inquiry_buyer_page.assert_text(inquiry_buyer_page.get_comment_info(), 'срочно')
        print("Тест: Комментарий в запросе отображается верно")
        print("Тест: Поля заполнены в соотвествии с запросом")

        # проверили позиции
        inquiry_buyer_page.assert_items_of_list(inquiry_buyer_page.get_names_positions_info(), names_products_inquiry)
        print("Тест: Товары в отправленном запросе = товарам в информации о запросе")

        # проверили единицы измерения
        inquiry_buyer_page.assert_items_of_list(inquiry_buyer_page.get_units_positions_info(), units_inquiry)
        print("Тест: Единицы измерения в отправленном запросе = единицам в информации о запросе")

        # проверили кол-во
        inquiry_buyer_page.assert_lists(inquiry_buyer_page.get_quantity_positions_info(), quantity_products_inquiry)
        print("Тест: Кол-во товаров в отправленном запросе = кол-ву товаров в информации о запросе")

        print("================ПОСТАВЩИК================")

        # разлогинились
        inquiry_buyer_page.click_element(main_page.get_logout())

        # нажали Войти на главной странице
        main_page.click_element(main_page.get_login())

        # авторизовались под поставщиком, приняли куки
        login_page.authorization(DataTest.login_correct_seller, DataTest.password_correct_seller)
        # main_page.agree_cookie()

        # отсортировали запросы по дате размещения
        inquiry_seller_page.sort_create()
        inquiry_seller_page.sort_create()
        time.sleep(2)

        print("================Проверка запроса================")

        # ищем верхний запрос сверяем время создателя наименование статус кол-во позиций
        inquiry_seller_page.assert_text(inquiry_seller_page.get_buyer_first(), 'ССР')
        print("Тест: создатель- покупатель в запросе отображается верно")
        inquiry_seller_page.assert_text(inquiry_seller_page.get_seller_first(), name_seller)
        print("Тест: исполнитель- поставщик в запросе отображается верно")
        inquiry_seller_page.assert_text(inquiry_seller_page.get_number_positions(), '10')
        print("Тест: Кол-во позиций в запросе 10")
        inquiry_seller_page.assert_time_in_range(inquiry_seller_page.datetime_create(), datetime_request_minus5sec,
                                                 datetime_request_plus5sec)
        print("Тест: Время размещения запроса отображается верно")
        inquiry_seller_page.assert_text(inquiry_seller_page.get_inquiry_status(), 'ожидает')
        print("Тест: Статус запроса ожидает")

        print("================Проверка информации по запросу================")

        # переходим в Информацию по запросу через троеточие
        inquiry_seller_page.click_element(inquiry_seller_page.get_vertical_dots())
        inquiry_seller_page.click_element(inquiry_seller_page.get_information())

        # в окне информации сверяем поля
        # проверили поля
        inquiry_seller_page.assert_value_attribute(inquiry_seller_page.get_buyer_info(), 'value', 'ССР/ИНН 7729790409')
        print("Тест: Покупатель в запросе отображается верно")
        inquiry_seller_page.assert_value_attribute(inquiry_seller_page.get_recipient_info(), 'value', 'Петров П.П.')
        print("Тест: Грузополучатель в запросе отображается верно")
        inquiry_seller_page.assert_value_attribute(inquiry_seller_page.get_yes_no_delivery_info(), 'value', 'нет')
        inquiry_seller_page.assert_value_attribute(inquiry_seller_page.get_address_info(), 'value', '-')
        print("Тест: Выбран самовывоз")
        inquiry_seller_page.assert_value_attribute(inquiry_seller_page.get_delay_payment_info(), 'value', '10')
        print("Тест: Отсрочка в запросе отображается верно")
        inquiry_seller_page.assert_value_attribute(inquiry_seller_page.get_seller_info(), 'value', '-')
        print("Тест: Поставщик в запросе отображается верно")
        inquiry_seller_page.assert_text(inquiry_seller_page.get_comment_info(), 'срочно')
        print("Тест: Комментарий в запросе отображается верно")
        print("Тест: Поля заполнены в соотвествии с запросом")

        # проверили позиции
        inquiry_seller_page.assert_items_of_list(inquiry_seller_page.get_names_positions_info(), names_products_inquiry)
        print("Тест: Товары в отправленном запросе = товарам в информации о запросе")

        # # проверили единицы измерения
        # inquiry_seller_page.assert_lists(inquiry_seller_page.get_units_positions_info(), units_inquiry)
        # print("Тест: Единицы измерения товаров в отправленном запросе = единицам измерения товаров в информации о запросе")

        # проверили кол-во
        inquiry_seller_page.assert_lists(inquiry_seller_page.get_quantity_positions_info(), quantity_products_inquiry)
        print("Тест: Кол-во товаров в отправленном запросе = кол-ву товаров в информации о запросе")

        # Вышли из информации по запросу
        inquiry_seller_page.click_element(inquiry_seller_page.get_exit_information())

        # выбрали запрос
        inquiry_seller_page.click_element(inquiry_seller_page.get_checkbox_inquiry())

        # нажали отправить счет
        inquiry_seller_page.click_element(inquiry_seller_page.get_send_invoice())

        print("================Проверка окна создания счета================")

        # в окне создания счета проверям доставку
        inquiry_seller_page.assert_value_attribute(inquiry_seller_page.get_radio_no_delivery(), 'checked', 'true')
        print("Тест: выбран самовывоз")

        # проверили позиции
        names_products_invoice = inquiry_seller_page.get_names_positions()
        inquiry_seller_page.assert_items_of_list(names_products_invoice, names_products_inquiry)
        print("Тест: Товары в отправленном запросе = товарам в счете")

        # проверили единицы измерения
        units_invoice = inquiry_seller_page.get_units_positions()
        # inquiry_seller_page.assert_lists(units_invoice, units_inquiry)
        # print("Тест: Единицы измерения товаров в отправленном запросе = единицам измерения товаров в счете")

        # проверили кол-во
        quantity_products_invoice = inquiry_seller_page.get_quantity_positions()
        inquiry_seller_page.assert_lists(quantity_products_invoice, quantity_products_inquiry)
        print("Тест: Кол-во товаров в отправленном запросе = кол-ву товаров в счете")

        # выбираем адрес и проверяем
        inquiry_seller_page.input_field(inquiry_seller_page.get_address(), 'москва')
        first_address_from_dropdown = inquiry_seller_page.get_address_from_dropdown().text
        inquiry_seller_page.click_element(inquiry_seller_page.get_address_from_dropdown())
        inquiry_seller_page.assert_value_attribute(inquiry_seller_page.get_address(), 'value', first_address_from_dropdown)
        print("Тест: выбранный адрес самовывоза в поле")

        # заполняем поля
        inquiry_seller_page.input_field(inquiry_seller_page.get_title(), '1')
        inquiry_seller_page.input_field(inquiry_seller_page.get_prepayment(), '100')
        inquiry_seller_page.input_field(inquiry_seller_page.get_payment_deferment(), '10')

        # прикрепляем файл
        path = Path(pathlib.Path.cwd(), 'file.ods')
        inquiry_seller_page.clear_hidden(inquiry_seller_page.get_file())
        inquiry_seller_page.input_field(inquiry_seller_page.get_file(), str(path))
        inquiry_seller_page.assert_value_attribute(inquiry_seller_page.get_title_file(), 'title', 'file.ods')
        print("Тест: файл прикреплен к счету")

        # заполняем цены и сохраняем их в список
        prices_invoice = inquiry_seller_page.input_price()
        # print(prices_invoice)

        # Выбрать все позиции
        inquiry_seller_page.check_all_positions()

        # нажимаем отправить счет
        inquiry_seller_page.click_element(inquiry_seller_page.get_send_invoice_2())

        # нажимаем отправить в окне нотификации
        inquiry_seller_page.click_element(inquiry_seller_page.get_send_notification())
        time.sleep(5)

        print("================Проверка смены статусов по запросу================")

        # проверяем статус запроса и счета отправлен отправлен
        inquiry_seller_page.assert_text(inquiry_seller_page.get_inquiry_status(), 'отправлен')
        print("Тест: Статус счета отправлен")
        inquiry_seller_page.assert_text(inquiry_seller_page.get_invoice_status(), 'Отправлен')
        print("Тест: Статус запроса отправлен")

        # через троеточие переходим в посмотреть счет
        inquiry_seller_page.click_element(inquiry_seller_page.get_vertical_dots())
        inquiry_seller_page.click_element(inquiry_seller_page.get_information())
        inquiry_seller_page.click_element(inquiry_seller_page.get_look_invoice())
        time.sleep(5)

        print("================Проверка вкладки Посмотреть счет================")

        # сверяем счет
        # номер счета, предоплата, отсрочка,адрес
        inquiry_seller_page.assert_value_attribute(inquiry_seller_page.get_title_invoice(), 'value', '1')
        inquiry_seller_page.assert_value_attribute(inquiry_seller_page.get_address_invoice(), 'value',
                                                   first_address_from_dropdown)
        inquiry_seller_page.assert_value_attribute(inquiry_seller_page.get_prepayment_invoice(), 'value', '100')
        inquiry_seller_page.assert_value_attribute(inquiry_seller_page.get_payment_deferment_invoice(), 'value', '10')
        print("Тест: Поля заполнены в соотвествии со счетом")

        # файл
        inquiry_seller_page.assert_value_attribute(inquiry_seller_page.get_title_file_invoice(), 'title', 'file.ods')
        print("Тест: файл прикреплен к счету")

        # проверили позиции
        inquiry_seller_page.assert_items_of_list(inquiry_seller_page.get_names_positions_invoice(), names_products_invoice)
        print("Тест: Товары в отправленном счете = товарам в счете")

        # проверили единицы измерения
        inquiry_seller_page.assert_lists(inquiry_seller_page.get_units_positions_invoice(), units_invoice)
        print("Тест: Единицы измерения товаров в отправленном счете = единицам измерения товаров в счете")

        # проверили кол-во
        inquiry_seller_page.assert_lists(inquiry_seller_page.get_quantity_positions_invoice(), quantity_products_invoice)
        print("Тест: Кол-во товаров в отправленном счете = кол-ву товаров в счете")

        # проверили цены
        inquiry_seller_page.assert_lists(inquiry_seller_page.get_prices_positions_invoice(), prices_invoice)
        print("Тест: Цены товаров в отправленном счете = ценам товаров в счете")




