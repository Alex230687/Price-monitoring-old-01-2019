import xlrd
import os
import datetime


class LoaderDeleter(object):
    def __init__(self, connection, cursor):
        self.connection = connection
        self.cursor = cursor
        self.data_for_load_base_path = r'..\ПАРСИНГ\Исходные данные'
        self.indicator = ''
        self.rrc_data = self.get_rrc_data()
        self.new_data = self.get_new_data()
        self.best_data = self.get_best_data()

    def get_rrc_data(self):
        wb_rrcbooks = xlrd.open_workbook(os.path.normpath(os.path.join(self.data_for_load_base_path, 'rrc.xlsx')))
        ws_rrcbooks = wb_rrcbooks.sheet_by_index(0)

        def row_data(row):
            rows = [ws_rrcbooks.cell(row, 1).value, ws_rrcbooks.cell(row, 2).value,
                    ws_rrcbooks.cell(row, 4).value, int(ws_rrcbooks.cell(row, 5).value), ]
            return rows

        data_for_sql_load = [row_data(row) for row in range(1, ws_rrcbooks.nrows)]
        return data_for_sql_load

    def get_new_data(self):
        wb_newbooks = xlrd.open_workbook(os.path.normpath(os.path.join(self.data_for_load_base_path, 'new.xlsx')))
        ws_newbooks = wb_newbooks.sheet_by_index(0)

        def row_data(row):
            date_cell = xlrd.xldate_as_tuple(ws_newbooks.cell(row, 4).value, wb_newbooks.datemode)
            rows = [ws_newbooks.cell(row, 0).value, ws_newbooks.cell(row, 1).value,
                    ws_newbooks.cell(row, 2).value, ws_newbooks.cell(row, 3).value,
                    datetime.date(date_cell[0], date_cell[1], date_cell[2]).isoformat(),
                    float(ws_newbooks.cell(row, 5).value), ]
            return rows

        data_for_sql_load = [row_data(row) for row in range(1, ws_newbooks.nrows)]
        return data_for_sql_load

    def get_best_data(self):
        wb_bestbooks = xlrd.open_workbook(os.path.normpath(os.path.join(self.data_for_load_base_path, 'best.xlsx')))
        ws_bestbooks = wb_bestbooks.sheet_by_index(0)

        def row_data(row):
            rows = [ws_bestbooks.cell(row, 0).value, ws_bestbooks.cell(row, 1).value,
                    ws_bestbooks.cell(row, 2).value, ws_bestbooks.cell(row, 3).value,
                    float(ws_bestbooks.cell(row, 4).value), ]
            return rows

        data_for_sql_load = [row_data(row) for row in range(1, ws_bestbooks.nrows)]
        return data_for_sql_load

    def load_rrc_data(self):
        delete_query = "DELETE FROM dbo.rrc_block"
        load_query = "INSERT INTO dbo.rrc_block (author, title, isbn, price) VALUES (?, ?, ?, ?)"
        try:
            self.cursor.execute(delete_query)
        except:
            self.indicator = 'Ошибка удаления данных'
        else:
            self.connection.commit()
            try:
                self.cursor.executemany(load_query, self.rrc_data)
            except:
                self.indicator = "Данные удалены, ошибка загрузки новыз данных"
            else:
                self.connection.commit()
                self.indicator = "Данные успешно загружены"

    def load_new_data(self):
        date_monitoring_start = self.new_data[0][4]
        sql_date_check_query = 'SELECT MAX(date_start) FROM dbo.new_block'
        try:
            self.cursor.execute(sql_date_check_query)
        except:
            print('Ошибка запроса к БД')
        else:
            last_sql_date = self.cursor.fetchall()
            check_sql_date = last_sql_date[0][0]

            if date_monitoring_start != check_sql_date:

                sql_query_new = 'INSERT INTO dbo.new_block VALUES (?,?,?,?,?,?)'
                try:
                    self.cursor.executemany(sql_query_new, self.new_data)
                except:
                    print('Ошибка загрузки данных')
                else:
                    self.connection.commit()
            else:
                pass

    def load_best_data(self):
        delete_query = "DELETE FROM dbo.best_block"
        load_query = "INSERT INTO dbo.best_block VALUES (?, ?, ?, ?, ?)"
        try:
            self.cursor.execute(delete_query)
        except:
            self.indicator = 'Ошибка удаления данных'
        else:
            self.connection.commit()
            try:
                self.cursor.executemany(load_query, self.best_data)
            except:
                self.indicator = "Данные удалены, ошибка загрузки новыз данных"
            else:
                self.connection.commit()
                self.indicator = "Данные успешно загружены"

    def data_update_to_customers(self):
        table_list = [table.table_name for table in self.cursor.tables() if 'customer' in table.table_name]
        for table in table_list:
            sql_query = """INSERT INTO {0} (isbn)
                        (SELECT isbn FROM dbo.rrc_block WHERE isbn not in (SELECT isbn FROM {0})
                        UNION
                        SELECT isbn FROM dbo.new_block WHERE isbn not in (SELECT isbn FROM {0})
                        UNION
                        SELECT isbn FROM dbo.best_block WHERE isbn not in (SELECT isbn FROM {0}))""".format(table)
            try:
                self.cursor.execute(sql_query)
            except:
                pass
            else:
                self.connection.commit()

    def delete_all_rows(self):
        pass
