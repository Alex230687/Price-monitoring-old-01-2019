from base_customer_class import BaseCustomerClass
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from regex_modul import number_transform, isbn_to_barcode


class Customer01(BaseCustomerClass):
    sql_table_name = 'dbo.customer01'

    def __init__(self, key, connection, cursor):
        BaseCustomerClass.__init__(self, key, connection, cursor)
        self.table = Customer01.sql_table_name
        self.get_sql_row()

    def start_price_search(self, driver):
        if self.transaction_control and (self.link != '0' and self.link != 0):
            try:
                driver.get(self.link)
                time.sleep(3)
                WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
                    (By.XPATH, "//div[@class='price js-product-price on-page']")))
                time.sleep(2)
                tag = driver.find_elements_by_xpath("//div[@class='price js-product-price on-page']")
                if tag:
                    price = number_transform(tag[0].text)
                    self.np = price
                    time.sleep(0.5)
                else:
                    return None
            except:
                return None
        else:
            return None

    def start_link_search(self, driver):
        """Поиск артикулов по сайту невозможен"""
        pass


class Customer02(BaseCustomerClass):
    sql_table_name = 'dbo.customer02'

    def __init__(self, key, connection, cursor):
        BaseCustomerClass.__init__(self, key, connection, cursor)
        self.table = Customer02.sql_table_name
        self.get_sql_row()

    def start_price_search(self, driver):
        if self.transaction_control and (self.link != '0' and self.link != 0):
            try:
                driver.get(self.link)
                time.sleep(2)
                WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(
                    (By.XPATH, "//div[@*='offer-cart']/div/div/div/div/div/div/div/div/span/span")))
                tag = driver.find_elements_by_xpath("//div[@*='offer-cart']/div/div/div/div/div/div/div/div/span/span")
                if len(tag) == 1:
                    price = number_transform(tag[0].text)
                    self.np = price
                elif len(tag) == 2:
                    action = number_transform(tag[0].text)
                    self.ap = action
                    price = number_transform(tag[1].text)
                    self.np = price
                else:
                    pass
            except:
                return None
        else:
            return None

    def start_link_search(self, driver):
        """Поиск артикулов по сайту Временно недоступен, блокировка капчей"""
        pass


class Customer03(BaseCustomerClass):
    sql_table_name = 'dbo.customer03'

    def __init__(self, key, connection, cursor):
        BaseCustomerClass.__init__(self, key, connection, cursor)
        self.table = Customer03.sql_table_name
        self.get_sql_row()

    def start_price_search(self, driver):
        if self.transaction_control and (self.link != '0' and self.link != 0):
            try:
                driver.get(self.link)
                time.sleep(1)
                WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//h3")))
                tag = driver.find_elements_by_tag_name('h3')
                if tag:
                    price = number_transform(tag[0].text)
                    self.np = price
            except:
                pass
        else:
            pass

    def start_link_search(self, driver):
        if self.transaction_control and (self.link == '0' or self.link == 0):
            try:
                driver.get('https://www.customer03.ru/search.shtml')
                time.sleep(0.5)
                tag = driver.find_elements_by_xpath("//input[@id='search' and @type='text' and @name='keywords']")
                if tag:
                    tag[0].clear()
                    tag[0].send_keys(self.isbn)
                    btn = driver.find_elements_by_xpath("//button[@type='submit']")
                    if btn:
                        btn[0].click()
                        time.sleep(0.5)
                        link = driver.find_elements_by_xpath("//h2[@class='search-list-book-title']//a")
                        if link:
                            self.link = link[0].get_attribute('href')
            except:
                pass
        else:
            pass


class Customer04(BaseCustomerClass):
    sql_table_name = 'dbo.customer04'

    def __init__(self, key, connection, cursor):
        BaseCustomerClass.__init__(self, key, connection, cursor)
        self.table = Customer03.sql_table_name
        self.get_sql_row()

    def start_price_search(self, driver):
        if self.transaction_control and (self.link != '0' and self.link != 0):
            try:
                driver.get(self.link)
                time.sleep(1)
                WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div#price")))
                tag = driver.find_elements_by_css_selector("div#price")
                if tag:
                    price = number_transform(tag[0].text)
                    self.np = price
                tag_shop = driver.find_elements_by_css_selector("div#old_price")
                if tag_shop:
                    shop = number_transform(tag_shop[0].text)
                    self.sp = shop
            except:
                pass
        else:
            pass

    def start_link_search(self, driver):
        if self.transaction_control and (self.link == '0' or self.link == 0):
            try:
                driver.get('https://www.customer04.ru/')
                time.sleep(0.5)
                sr = driver.find_elements_by_css_selector("input#SearchBooks")
                if sr:
                    sr[0].send_keys(self.isbn)
                    btn = driver.find_elements_by_css_selector("button#SearchButton")
                    if btn:
                        btn[0].click()
                        time.sleep(0.5)
                        link = driver.find_elements_by_css_selector("div.row div.product a.img_link")
                        if link:
                            self.link = link[0].get_attribute('href')
            except:
                pass
        else:
            pass


class Customer05(BaseCustomerClass):
    sql_table_name = 'dbo.customer05'

    def __init__(self, key, connection, cursor):
        BaseCustomerClass.__init__(self, key, connection, cursor)
        self.table = Customer05.sql_table_name
        self.get_sql_row()

    def start_price_search(self, driver):
        if self.transaction_control and (self.link != '0' and self.link != 0):
            try:
                driver.get(self.link)
                time.sleep(2)
                WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(
                    (By.CSS_SELECTOR, "div.final-price-block")))
                time.sleep(0.5)
                tag = driver.find_elements_by_css_selector('span.old-price')
                if tag:
                    price = number_transform(tag[0].text)
                    self.np = price
                    tag2 = driver.find_elements_by_css_selector('div.final-price-block')
                    if tag2:
                        action = number_transform(tag2[0].text)
                        self.ap = action
                else:
                    tag3 = driver.find_elements_by_css_selector('div.final-price-block')
                    if tag3:
                        price = number_transform(tag3[0].text)
                        self.np = price
            except:
                pass
        else:
            pass

    def start_link_search(self, driver):
        """Поиск артикулов по сайту невозможен необходима подставнока артикулов поставщика"""
        pass


class Customer06(BaseCustomerClass):
    sql_table_name = 'dbo.customer06'

    def __init__(self, key, connection, cursor):
        BaseCustomerClass.__init__(self, key, connection, cursor)
        self.table = Customer06.sql_table_name
        self.get_sql_row()

    def start_price_search(self, driver):
        if self.transaction_control and (self.link != '0' and self.link != 0):
            try:
                driver.get(self.link)
                time.sleep(1)
                WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(
                    (By.XPATH, "//div[@class='yprice price']")))
                tag = driver.find_elements_by_xpath("//span[@class='price-old']//span[@class='price']")
                if tag:
                    price = number_transform(tag[0].text)
                    self.np = price
                    tag_two = driver.find_elements_by_xpath("//div[@class='yprice price']")
                    if tag_two:
                        action = number_transform(tag_two[0].text)
                        self.ap = action
                else:
                    tag_three = driver.find_elements_by_xpath("//div[@class='yprice price']")
                    if tag_three:
                        price = number_transform(tag_three[0].text)
                        self.np = price
            except:
                pass
        else:
            pass

    def start_link_search(self, driver):
        if self.transaction_control and (self.link == '0' or self.link == 0):
            try:
                driver.get('https://www.customer06.ru/search_form.php')
                time.sleep(1)
                tag = driver.find_elements_by_xpath("//input[@value and @name='s[isbn]']")
                if tag:
                    tag[0].send_keys(self.isbn)
                    btn = driver.find_elements_by_xpath(
                        "//input[@value='Найти' and @class='submit' and @alt='Найти']")
                    if btn:
                        btn[0].click()
                        time.sleep(0.5)
                        link = driver.current_url
                        if '/books/' in link:
                            self.link = link
            except:
                try:
                    driver.get('https://www.customer06.ru/search_form.php')
                    time.sleep(1)
                    popup_window = driver.find_elements_by_xpath("//*[contains(text(), 'Я уже с вами')]")
                    if popup_window:
                        popup_window[0].click()
                        time.sleep(0.5)
                        tag = driver.find_elements_by_xpath("//input[@value and @name='s[isbn]']")
                        if tag:
                            tag[0].send_keys(self.isbn)
                            btn = driver.find_elements_by_xpath(
                                "//input[@value='Найти' and @class='submit' and @alt='Найти']")
                            if btn:
                                btn[0].click()
                                time.sleep(0.5)
                                link = driver.current_url
                                if '/books/' in link:
                                    self.link = link
                except:
                    pass
        else:
            pass


class Customer07(BaseCustomerClass):
    sql_table_name = 'dbo.customer07'

    def __init__(self, key, connection, cursor):
        BaseCustomerClass.__init__(self, key, connection, cursor)
        self.table = Customer07.sql_table_name
        self.get_sql_row()

    def start_price_search(self, driver):
        if self.transaction_control and (self.link != '0' and self.link != 0):
            try:
                driver.get(self.link)
                time.sleep(3)
                WebDriverWait(driver, 5).until(EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "div.xy")))
                time.sleep(2)

                tag = driver.find_elements_by_css_selector('div.xy span.Av')
                if tag:
                    price = number_transform(tag[0].text)
                    self.np = price
                    tag2 = driver.find_elements_by_css_selector('div.xy div.Cv')
                    if tag2:
                        action = number_transform(tag2[0].text)
                        self.ap = action
                else:
                    tag3 = driver.find_elements_by_css_selector('div.xy')
                    if tag3:
                        price = number_transform(tag3[0].text)
                        self.np = price
            except:
                pass
        else:
            pass

    def start_link_search(self, driver):
        if self.transaction_control and (self.link == '0' or self.link == 0):
            barcode = isbn_to_barcode(self.isbn)
            if barcode:
                try:
                    driver.get('https://www.customer07.ru/books?q=' + barcode)
                    tag = driver.find_elements_by_css_selector('div#books a[href*="www.customer07.ru/book?"]')
                    if tag:
                        link = tag[0].get_attribute('href')
                        if link:
                            self.link = link
                except:
                    pass
        else:
            pass


class Customer08(BaseCustomerClass):
    sql_table_name = 'dbo.customer08'

    def __init__(self, key, connection, cursor):
        BaseCustomerClass.__init__(self, key, connection, cursor)
        self.table = Customer08.sql_table_name
        self.get_sql_row()

    def start_price_search(self, driver):
        if self.transaction_control and (self.link != '0' and self.link != 0):
            try:
                driver.get(self.link)
                time.sleep(1)
                WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(
                    (By.XPATH, "//div[@class='order_block']/div[@class='price']/strong")))
                tag = driver.find_elements_by_xpath("//div[@class='order_block']//div[@class='price']//span")
                if tag:
                    price = number_transform(tag[0].text)
                    self.np = price
                    tag_two = driver.find_elements_by_xpath("//div[@class='order_block']/div[@class='price']/strong")
                    if tag_two:
                        action = number_transform(tag_two[0].text)
                        self.ap = action
                else:
                    tag_three = driver.find_elements_by_xpath("//div[@class='order_block']/div[@class='price']/strong")
                    if tag_three:
                        price = number_transform(tag_three[0].text)
                        self.np = price
                tag_shop = driver.find_elements_by_xpath("//div[@class='rozn']/div[@class='price']/strong")
                if tag_shop:
                    shop = number_transform(tag_shop[0].text)
                    self.sp = shop
            except:
                pass
        else:
            pass

    def start_link_search(self, driver):
        if self.transaction_control and (self.link == '0' or self.link == 0):
            try:
                driver.get('https://customer08.ru/search/?q=' + self.isbn)
                tag = driver.find_elements_by_xpath("//div[@class='product']//a")
                if tag:
                    link = tag[0].get_attribute('href')
                    if link:
                        if '/product/' in link:
                            self.link = link
            except:
                pass
        else:
            pass


class Customer09(BaseCustomerClass):
    sql_table_name = 'dbo.customer09'

    def __init__(self, key, connection, cursor):
        BaseCustomerClass.__init__(self, key, connection, cursor)
        self.table = Customer09.sql_table_name
        self.get_sql_row()

    def start_price_search(self, driver):
        if self.transaction_control and (self.link != '0' and self.link != 0):
            try:
                driver.get(self.link)
                time.sleep(3)
                try:
                    city_tag = driver.find_element_by_xpath("//a[@id='cityYes']")
                    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                except:
                    pass
                time.sleep(0.5)
                WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(
                    (By.XPATH, "//*[@class='product__price']//div[@class='price']")))
                tag = driver.find_elements_by_xpath("//*[@class='product__price']//div[@class='old-price']")
                if tag:
                    price = number_transform(tag[0].text)
                    self.np = price
                    tag_two = driver.find_elements_by_xpath("//*[@class='product__price']//div[@class='price']")
                    if tag_two:
                        action = number_transform(tag_two[0].text)
                        self.ap  = action
                else:
                    tag_three = driver.find_elements_by_xpath("//*[@class='product__price']//div[@class='price']")
                    if tag_three:
                        price = number_transform(tag_three[0].text)
                        self.np = price
            except:
                pass
        else:
            pass

    def start_link_search(self, driver):
        if self.transaction_control and (self.link == '0' or self.link == 0):
            barcode = isbn_to_barcode(self.isbn)
            if barcode:
                try:
                    driver.get('https://www.customer09.ru/search/result/?page=1')
                    tag = driver.find_elements_by_xpath("//form[@action='/search/result/']//input[@type='text']")
                    if tag:
                        tag[0].send_keys(barcode)
                        btn = driver.find_elements_by_xpath("//form[@action='/search/result/']//button")
                        if btn:
                            btn[0].click()
                            time.sleep(0.5)
                            tag_two = driver.find_elements_by_xpath(
                                "//div[contains(@class, 'product-card__info')]//a[contains(@href, '/catalog/')]")
                            if tag_two:
                                link = tag_two[0].get_attribute('href')
                                if link:
                                    self.link = link
                except:
                    try:
                        driver.get('https://www.customer09.ru/search/result/?page=1')
                        popup_window = driver.find_elements_by_xpath("//a[@id='cityYes']")
                        if popup_window:
                            if popup_window[0].is_displayed():
                                popup_window[0].click()
                                time.sleep(0.5)
                                tag = driver.find_elements_by_xpath(
                                    "//form[@action='/search/result/']//input[@type='text']")
                                if tag:
                                    tag[0].send_keys(barcode)
                                    btn = driver.find_elements_by_xpath("//form[@action='/search/result/']//button")
                                    if btn:
                                        btn[0].click()
                                        time.sleep(0.5)
                                        tag_two = driver.find_elements_by_xpath(
                                            "//div[contains(@class, 'product-card__info')]//a[contains(@href, '/catalog/')]")
                                        if tag_two:
                                            link = tag_two[0].get_attribute('href')
                                            if link:
                                                self.link = link
                    except:
                        pass
        else:
            pass


class Customer10(BaseCustomerClass):
    sql_table_name = 'dbo.customer10'

    def __init__(self, key, connection, cursor):
        BaseCustomerClass.__init__(self, key, connection, cursor)
        self.table = Customer10.sql_table_name
        self.get_sql_row()

    def start_price_search(self, driver):
        if self.transaction_control and (self.link != '0' and self.link != 0):
            try:
                driver.get(self.link)
                time.sleep(1)
                tag = driver.find_elements_by_xpath("//div[@id='product_price']")
                if tag:
                    price = number_transform(tag[0].text)
                    self.np = price
            except:
                pass
        else:
            pass

    def start_link_search(self, driver):
        if self.transaction_control and (self.link == '0' or self.link == 0):
            try:
                driver.get('http://www.customer10.ru/advsearch/')
                tag = driver.find_elements_by_xpath("//*[@type='text' and @name='isbn']")
                if tag:
                    tag[0].send_keys(self.isbn)
                    btn = driver.find_elements_by_xpath("//*[@type='button' and @value='поиск']")
                    if btn:
                        btn[0].click()
                        time.sleep(0.5)
                        tag_two = driver.find_elements_by_xpath("//*[@class='good_book']//figure//a")
                        if tag_two:
                            link = tag_two[0].get_attribute('href')
                            if link:
                                self.link = link
            except:
                pass
        else:
            pass


class Customer11(BaseCustomerClass):
    sql_table_name = 'dbo.customer11'

    def __init__(self, key, connection, cursor):
        BaseCustomerClass.__init__(self, key, connection, cursor)
        self.table = Customer11.sql_table_name
        self.get_sql_row()

    def start_price_search(self, driver):
        if self.transaction_control and (self.link != '0' and self.link != 0):
            try:
                driver.get(self.link)
                time.sleep(1)
                WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
                    (By.XPATH, "//div[@class='product-prices']/span")))
                tag = driver.find_elements_by_xpath("//div[@class='product-prices']/span")
                if len(tag) == 2 and tag[1].text:
                    price = number_transform(tag[1].text)
                    self.np = price
                    action = number_transform(tag[0].text)
                    self.ap = action
                elif len(tag) == 2 and not tag[1].text:
                    price = number_transform(tag[0].text)
                    self.np = price
                else:
                    pass
            except:
                pass
        else:
            pass

    def start_link_search(self, driver):
        if self.transaction_control and (self.link == '0' or self.link == 0):
            barcode = isbn_to_barcode(self.isbn)
            if barcode:
                try:
                    driver.get('http://www.customer11.ru/search?q=' + barcode)
                    tag = driver.find_elements_by_xpath(
                        "//div[@class='products']//form//a[contains(@class, product_card)]")
                    if tag:
                        link = tag[0].get_attribute('href')
                        if link:
                            self.link = link
                except:
                    pass
        else:
            pass


class Customer12(BaseCustomerClass):
    sql_table_name = 'dbo.customer12'

    def __init__(self, key, connection, cursor):
        BaseCustomerClass.__init__(self, key, connection, cursor)
        self.table = Customer12.sql_table_name
        self.get_sql_row()

    def start_price_search(self, driver):
        if self.transaction_control and (self.link != '0' and self.link != 0):
            try:
                driver.get(self.link)
                time.sleep(0.5)
                WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(
                    (By.XPATH, "//div[@class='detail-price-val']")))
                tag = driver.find_elements_by_xpath("//div[@class='detail-price-val']")
                if tag:
                    price = number_transform(tag[0].text)
                    self.np = price
            except:
                pass
        else:
            pass

    def start_link_search(self, driver):
        """Поиска артикулов по сайту невозможен"""
        pass


class Customer13(BaseCustomerClass):
    sql_table_name = 'dbo.customer13'

    def __init__(self, key, connection, cursor):
        BaseCustomerClass.__init__(self, key, connection, cursor)
        self.table = Customer13.sql_table_name
        self.get_sql_row()

    def start_price_search(self, driver):
        if self.transaction_control and (self.link != '0' and self.link != 0):
            try:
                driver.get(self.link)
                time.sleep(0.5)
                WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(
                    (By.CSS_SELECTOR, "div.container-semiboxed div.row")))
                tag = driver.find_elements_by_css_selector('div.container-semiboxed div.row div.g-mb-20 s')
                if tag:
                    price = number_transform(tag[0].text)
                    self.np = price
                    tag2 = driver.find_elements_by_css_selector('div.container-semiboxed div.row div.g-mb-20 span')
                    if tag2:
                        action = number_transform(tag2[0].text)
                        self.ap = action
                else:
                    tag3 = driver.find_elements_by_css_selector('div.container-semiboxed div.row div.g-mb-20 span')
                    if tag3:
                        price = number_transform(tag3[0].text)
                        self.np = price
            except:
                pass
        else:
            pass

    def start_link_search(self, driver):
        """Поиск артикулов по сайту невозможен"""
        pass


class Customer14(BaseCustomerClass):
    sql_table_name = 'dbo.customer14'

    def __init__(self, key, connection, cursor):
        BaseCustomerClass.__init__(self, key, connection, cursor)
        self.table = Customer14.sql_table_name
        self.get_sql_row()

    def start_price_search(self, driver):
        if self.transaction_control and (self.link != '0' and self.link != 0):
            try:
                driver.get(self.link)
                time.sleep(1)
                WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(
                    (By.CSS_SELECTOR, "span.tg-bookprice")))
                time.sleep(1)
                tag = driver.find_elements_by_css_selector('span.tg-bookprice > del')
                if tag:
                    price = number_transform(tag[0].text)
                    self.np = price
                    tag2 = driver.find_elements_by_css_selector('span.tg-bookprice > ins')
                    if tag2:
                        action = number_transform(tag2[0].text)
                        self.ap = action
                else:
                    tag3 = driver.find_elements_by_css_selector('span.tg-bookprice > ins')
                    if tag3:
                        price = number_transform(tag3[0].text)
                        self.np = price
            except:
                pass
        else:
            pass

    def start_link_search(self, driver):
        if self.transaction_control and (self.link == '0' or self.link == 0):
            try:
                driver.get('http://customer14.ru/catalog?q=' + self.isbn)
                tag = driver.find_elements_by_xpath("//a[@class='tg-bookimg']")
                if tag:
                    link = tag[0].get_attribute('href')
                    if link:
                        self.link = link
            except:
                pass
        else:
            pass


class Customer15(BaseCustomerClass):
    sql_table_name = 'dbo.customer15'

    def __init__(self, key, connection, cursor):
        BaseCustomerClass.__init__(self, key, connection, cursor)
        self.table = Customer15.sql_table_name
        self.get_sql_row()

    def start_price_search(self, driver):
        if self.transaction_control and (self.link != '0' and self.link != 0):
            try:
                driver.get(self.link)
                time.sleep(0.5)
                WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(
                    (By.XPATH, "//div[@class='book__price']")))
                tag = driver.find_elements_by_xpath("//div[@class='book__price']")
                if tag:
                    price = number_transform(tag[0].text)
                    self.np = price
                tag_two = driver.find_elements_by_xpath("//div[@class='book__shop-details']")
                if tag_two:
                    tag_three = tag_two[0].find_elements_by_tag_name('noindex')
                    if tag_three:
                        shop = number_transform(tag_three[0].text)
                        self.sp = shop
            except:
                pass
        else:
            pass

    def start_link_search(self, driver):
        if self.transaction_control and (self.link == '0' or self.link == 0):
            try:
                driver.get('https://www.customer15.ru/search/')
                tag = driver.find_elements_by_xpath("//input[contains(@placeholder, 'Введите текст')]")
                if tag:
                    tag[0].send_keys(self.isbn)
                    btn = driver.find_elements_by_xpath(
                        "//input[contains(@placeholder, 'Введите текст')]//ancestor::form//button")
                    if btn:
                        btn[0].click()
                        time.sleep(0.5)
                        tag_two = driver.find_elements_by_xpath(
                            "//*[@class='book-preview']//*[@class='book-preview__cover']//a")
                        if tag_two:
                            link = tag_two[0].get_attribute('href')
                            if '/ebooks/' not in link:
                                self.link = link
            except:
                pass
        else:
            pass


class Customer16(BaseCustomerClass):
    sql_table_name = 'dbo.customer16'

    def __init__(self, key, connection, cursor):
        BaseCustomerClass.__init__(self, key, connection, cursor)
        self.table = Customer16.sql_table_name
        self.get_sql_row()

    def start_price_search(self, driver):
        if self.transaction_control and (self.link != '0' and self.link != 0):
            try:
                driver.get(self.link)
                time.sleep(0.5)
                WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(
                    (By.XPATH, "//b[@style='font-size:14px']")))
                tag = driver.find_elements_by_xpath("//b[@style='font-size:14px']")
                if tag:
                    price = number_transform(tag[0].text)
                    self.np = price
            except:
                pass
        else:
            pass

    def start_link_search(self, driver):
        if self.transaction_control and (self.link == '0' or self.link == 0):
            try:
                driver.get('https://customer16.ru/shop/search/b/')
                tag = driver.find_elements_by_xpath("//input[@name='isbn' and @type='text']")
                if tag:
                    tag[0].send_keys(self.isbn)
                    btn = driver.find_elements_by_xpath("//input[@class='bigbutton' and @type='submit']")
                    if btn:
                        btn[0].click()
                        time.sleep(0.5)
                        tag_two = driver.find_elements_by_xpath(
                            "//div[@class]//a[@title and contains(@href, '/shop/product/')]")
                        if tag_two:
                            link = tag_two[0].get_attribute('href')
                            if link:
                                self.link = link
            except:
                pass
        else:
            pass


class Customer17(BaseCustomerClass):
    sql_table_name = 'dbo.customer17'

    def __init__(self, key, connection, cursor):
        BaseCustomerClass.__init__(self, key, connection, cursor)
        self.table = Customer17.sql_table_name
        self.get_sql_row()

    def start_price_search(self, driver):
        if self.transaction_control and (self.link != '0' and self.link != 0):
            try:
                driver.get(self.link)
                time.sleep(2)
                WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(
                    (By.XPATH, "//span[@class='js__actualPrice']")))
                tag = driver.find_elements_by_xpath("//*[@class and contains(@title, 'Старая цена')]")
                if tag:
                    price = number_transform(tag[0].text)
                    self.np = price
                    tag_two = driver.find_elements_by_xpath("//span[@itemprop='price']")
                    if tag_two:
                        action = number_transform(tag_two[0].text)
                        self.ap = action
                else:
                    tag_three = driver.find_elements_by_xpath("//span[@class='js__actualPrice']")
                    if tag_three:
                        price = number_transform(tag_three[0].text)
                        self.np = price
            except:
                try:
                    WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(
                        (By.XPATH, "//*[@class and contains(@title, 'Старая цена')]")))
                    tag = driver.find_elements_by_xpath("//*[@class and contains(@title, 'Старая цена')]")
                    if tag:
                        price = number_transform(tag[0].text)
                        self.np = price
                        tag_two = driver.find_elements_by_xpath("//span[@itemprop='price']")
                        if tag_two:
                            action = number_transform(tag_two[0].text)
                            self.ap = action
                    else:
                        tag_three = driver.find_elements_by_xpath("//span[@class='js__actualPrice']")
                        if tag_three:
                            price = number_transform(tag_three[0].text)
                            self.np = price
                except:
                    pass
        else:
            pass

    def start_link_search(self, driver):
        if self.transaction_control and (self.link == '0' or self.link == 0):
            barcode = isbn_to_barcode(self.isbn)
            if barcode:
                try:
                    driver.get('https://www.customer17.ru/sitesearch.html?query=' + barcode)
                    time.sleep(1.5)
                    tag = driver.find_elements_by_xpath(
                        "//div[@class='indexGoods__item']//a[contains(@href, '/catalogue/')]")
                    if tag:
                        link = tag[0].get_attribute('href')
                        if link:
                            self.link = link
                except:
                    pass
        else:
            pass


class Customer18(BaseCustomerClass):
    sql_table_name = 'dbo.customer18'

    def __init__(self, key, connection, cursor):
        BaseCustomerClass.__init__(self, key, connection, cursor)
        self.table = Customer18.sql_table_name
        self.get_sql_row()

    def start_price_search(self, driver):
        if self.transaction_control and (self.link != '0' and self.link != 0):
            try:
                driver.get(self.link)
                time.sleep(1)
                WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(
                      (By.CSS_SELECTOR, "div.top-sale-block")))
                time.sleep(2)
                tag = driver.find_elements_by_css_selector('div.top-sale-block > div:first-child > div:first-child > div:first-child > div:first-child > div:first-child > div:first-child > div:first-child > div:first-child > span')
                if len(tag) == 1:
                    price = number_transform(tag[0].text)
                    self.np = price
                elif len(tag) == 2:
                    action = number_transform(tag[0].text)
                    self.ap = action
                    price = number_transform(tag[1].text)
                    self.np = price
            except:
                pass
        else:
            pass

    def start_link_search(self, driver):
        if self.transaction_control and (self.link == '0' or self.link == 0):
            barcode = isbn_to_barcode(self.isbn)
            if barcode:
                try:
                    driver.get('https://www.customer18.ru/search/?text=' + barcode)
                    time.sleep(2.5)
                    tag = driver.find_elements_by_css_selector('a.tile-wrapper')
                    if tag:
                        link = tag[0].get_attribute('href')
                        if link:
                            self.link = link
                except:
                    pass
        else:
            pass


class Customer19(BaseCustomerClass):
    sql_table_name = 'dbo.customer19'

    def __init__(self, key, connection, cursor):
        BaseCustomerClass.__init__(self, key, connection, cursor)
        self.table = Customer19.sql_table_name
        self.get_sql_row()

    def start_price_search(self, driver):
        if self.transaction_control and (self.link != '0' and self.link != 0):
            try:
                driver.get(self.link)
                time.sleep(0.5)
                WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(
                    (By.XPATH, "//span[@class='price']")))
                tag = driver.find_elements_by_xpath("//*[@class and contains(text(), 'Стандартная цена')]")
                if tag:
                    price = number_transform(tag[0].text)
                    self.np = price
                    tag_two = driver.find_elements_by_xpath("//span[@class='price']")
                    if tag_two:
                        action = number_transform(tag_two[0].text)
                        self.ap = action
                else:
                    tag_three = driver.find_elements_by_xpath("//span[@class='price']")
                    if tag_three:
                        price = number_transform(tag_three[0].text)
                        self.np = price
            except:
                pass
        else:
            pass

    def start_link_search(self, driver):
        if self.transaction_control and (self.link == '0' or self.link == 0):
            try:
                driver.get('http://www.customer19.ru/poisk.php')
                time.sleep(0.5)
                tag = driver.find_elements_by_xpath("//*[@name='isbn' and @type='text']")
                if tag:
                    tag[0].send_keys(self.isbn)
                    btn = driver.find_elements_by_xpath("//*[@type='submit' and @class='red_button']")
                    if btn:
                        btn[0].click()
                        time.sleep(0.5)
                        tag_two = driver.find_elements_by_xpath("//h2[@itemprop='name']//a")
                        if tag_two:
                            link = tag_two[0].get_attribute('href')
                            if link:
                                self.link = link
            except:
                pass
        else:
            pass


class Customer20(BaseCustomerClass):
    sql_table_name = 'dbo.customer20'

    def __init__(self, key, connection, cursor):
        BaseCustomerClass.__init__(self, key, connection, cursor)
        self.table = Customer20.sql_table_name
        self.get_sql_row()

    def start_price_search(self, driver):
        if self.transaction_control and (self.link != '0' and self.link != 0):
            try:
                driver.get(self.link)
                time.sleep(0.5)
                WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(
                    (By.CSS_SELECTOR, "div.content > p")))
                time.sleep(1)
                tag = driver.find_elements_by_css_selector('div.content > p')
                if tag:
                    if 'Возрастное ограничение' in tag[0].text:
                        form_check = driver.find_elements_by_css_selector('form[method="POST"] div.control input')
                        if form_check:
                            form_check[0].click()
                            form_btn = driver.find_elements_by_css_selector('form[method="POST"] div.control button')
                            if form_btn:
                                form_btn[0].click()
                                time.sleep(2)
                                tag2 = driver.find_elements_by_css_selector('div.content > p')
                                if len(tag2) == 2:
                                    price = number_transform(tag2[0].text)
                                    self.np = price
                                    print(price)
                                elif len(tag2) == 3:
                                    price = number_transform(tag2[0].text)
                                    self.np = price
                                    action = number_transform(tag2[1].text)
                                    self.ap = action
                                elif len(tag2) == 4:
                                    price = number_transform(tag2[0].text)
                                    self.np = price
                                    action = number_transform(tag2[2].text)
                                    self.ap = action
                    else:
                        if len(tag) == 2:
                            price = number_transform(tag[0].text)
                            self.np = price
                        elif len(tag) == 3:
                            price = number_transform(tag[0].text)
                            self.np = price
                            action = number_transform(tag[1].text)
                            self.ap = action
                        elif len(tag) == 4:
                            price = number_transform(tag[0].text)
                            self.np = price
                            action = number_transform(tag[2].text)
                            self.ap = action
            except:
                pass
        else:
            pass

    def start_link_search(self, driver):
        """Поиска артикулов по сайту невозможен"""
        pass


class_list = [
    Customer01,
    Customer02,
    Customer04,
    Customer05,
    Customer06,
    Customer07,
    Customer08,
    Customer09,
    Customer10,
    Customer11,
    Customer12,
    Customer13,
    Customer14,
    Customer15,
    Customer16,
    Customer17,
    Customer18,
    Customer19,
    Customer20,
]
