from sub_customer_classes import class_list
from driver_object import FastDriver, LongDriver
from pyodbc import Error


class Parser(object):
    def __init__(self, connection, cursor):
        #self.web_driver = FastDriver()
        #self.slow_web_driver = LongDriver()
        self.connection = connection
        self.cursor = cursor
        self.table_rrc = 'dbo.rrc_block'
        self.table_best = 'dbo.best_block'
        self.table_new = 'dbo.new_block'
        self.sql_data = self.get_sql_keys_list()

    def get_sql_keys_list(self):
        get_query = """SELECT isbn FROM {0}
                    UNION SELECT isbn FROM {1}
                    UNION SELECT isbn FROM {2}
                        WHERE 30>(SELECT DATEDIFF(DAY, date_start, GETDATE()))""".format(
                            self.table_rrc, self.table_best, self.table_new)
        try:
            self.cursor.execute(get_query)
        except Error as err:
            print(err)
            return None
        else:
            sql_rows = self.cursor.fetchall()
            if sql_rows:
                article_list = [row.isbn for row in sql_rows]
                return article_list
            else:
                return None

    def start_price_search_modul(self):
        driver = FastDriver()
        if self.sql_data:
            for key in self.sql_data:
                for cl in class_list:
                    customer = cl(key, self.connection, self.cursor)
                    customer.start_price_search(driver.driver)
                    customer.update_sql_price()
            driver.quit_driver()
        else:
            print('Список ключевых артикулов отсуствует, проверьте подключение к БД и синтаксис запроса')
            driver.quit_driver()

    def start_links_search_modul(self):
        driver = LongDriver()
        if self.sql_data:
            for key in self.sql_data:
                for cl in class_list:
                    customer = cl(key, self.connection, self.cursor)
                    customer.start_link_search(driver.driver)
                    customer.update_sql_link()
            driver.quit_driver()
        else:
            print('Список ключевых артикулов отсуствует, проверьте подключение к БД и синтаксис запроса')
            driver.quit_driver()

