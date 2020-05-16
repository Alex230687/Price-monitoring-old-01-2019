import pyodbc


class ConnectionObject(object):
    """CREATE CONNECTION ONBJET"""

    def __init__(self, args):
        self.settings = 'DRIVER={0};SERVER={1};DATABASE={2};UID={3};PWD={4};'.format(*args)
        self.connection = self.create_connection()
        self.cursor = self.create_cursor()

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def create_connection(self):
        create_connection = pyodbc.connect(self.settings)
        return create_connection

    def create_cursor(self):
        create_cursor = self.connection.cursor()
        return create_cursor
