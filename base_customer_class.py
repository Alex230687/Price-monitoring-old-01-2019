from pyodbc import Error


class BaseCustomerClass(object):
    def __init__(self, key, connection, cursor):
        self.connection = connection
        self.cursor = cursor
        self.transaction_control = None
        self.table = None
        self.link = None
        self.isbn = key
        self.np = 0
        self.sp = 0
        self.ap = 0

    def __del__(self):
        print('Экземпляр класса удалён')

    def start_price_search(self, driver):
        pass

    def start_link_search(self, driver):
        pass

    def get_sql_row(self):
        get_query = "SELECT link FROM {0} WHERE isbn='{1}'".format(self.table, self.isbn)
        try:
            self.cursor.execute(get_query)
        except Error as err:
            print(err)
            self.transaction_control = False
        else:
            sql_element = self.cursor.fetchone()
            if sql_element:
                self.link = sql_element.link
                self.transaction_control = True

    def update_sql_price(self):
        if self.transaction_control:
            post_query = "UPDATE {0} SET np={1}, sp={2}, ap={3} WHERE isbn='{4}'".format(
                self.table, self.np, self.sp, self.ap, self.isbn)
            try:
                self.cursor.execute(post_query)
            except Error as err:
                print(err)
                print('Данные таблицы {} по артикулу {} не обновлены'.format(self.table, self.isbn))
            else:
                self.connection.commit()
        else:
            print('первичный этап запроса данных не пройден, дальшешая работа с экземпляром невозможна')

    def update_sql_link(self):
        if self.transaction_control:
            if self.link and self.link != '0':
                post_query = "UPDATE {0} SET link='{1}' WHERE isbn='{2}'".format(
                    self.table, self.link, self.isbn)
                try:
                    self.cursor.execute(post_query)
                except Error as err:
                    print(err)
                    print('Данные таблицы {} по артикулу {} не обновлены'.format(self.table, self.isbn))
                else:
                    self.connection.commit()
            else:
                print('текущее значение параметра link равно 0, запись в sql не производится')
        else:
            print('первичный этап запроса данных не пройден, дальшешая работа с экземпляром невозможна')
