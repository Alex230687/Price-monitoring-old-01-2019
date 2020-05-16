from PyQt5 import QtCore, QtWidgets
from connection_object import ConnectionObject
from data_for_test import settings_express
from dashboard_object import Report
from data_load_to_sql_modul import LoaderDeleter
from parser_object import Parser
import time
import datetime
import os


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.today = self.current_date()
        self.base_dir = r'C:\Users\asebekin\Desktop\ПАРСИНГ'
        self.label3 = QtWidgets.QLabel('Запуск ПАРСЕРА')
        self.button_run = QtWidgets.QPushButton('ПОИСК ЦЕН (УТРО)')
        self.button_run_lnk = QtWidgets.QPushButton('ПОИСК ССЫЛОК (ВЕЧЕР)')
        self.label2 = QtWidgets.QLabel('Загрузить новые списки')
        self.button_load_rrc = QtWidgets.QPushButton('ЗАГРУЗИТЬ РРЦ')
        self.button_load_new = QtWidgets.QPushButton('ЗАГРУЗИТЬ НОВИНКИ')
        self.button_load_best = QtWidgets.QPushButton('ЗАГРУЗИТЬ БЕСТСЕЛЛЕРЫ')
        self.button_load_all = QtWidgets.QPushButton('ОБНОВИТЬ ДАННЫЕ')
        self.label = QtWidgets.QLabel('Тестовый интерфейс')
        self.button_path = QtWidgets.QPushButton('СОЗДАТЬ ПАПКУ')
        self.button = QtWidgets.QPushButton('РРЦ')
        self.button2 = QtWidgets.QPushButton('НОВИНКИ')
        self.button3 = QtWidgets.QPushButton('БЕСТСЕЛЛЕРЫ')
        self.button4 = QtWidgets.QPushButton('НАРУШЕНИЯ')
        self.button5 = QtWidgets.QPushButton('СКРИНШОТЫ')
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label3)
        self.vbox.addWidget(self.button_run)
        self.vbox.addWidget(self.button_run_lnk)
        self.vbox.addWidget(self.label2)
        self.vbox.addWidget(self.button_load_rrc)
        self.vbox.addWidget(self.button_load_new)
        self.vbox.addWidget(self.button_load_best)
        self.vbox.addWidget(self.button_load_all)
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.button_path)
        self.vbox.addWidget(self.button)
        self.vbox.addWidget(self.button2)
        self.vbox.addWidget(self.button3)
        self.vbox.addWidget(self.button4)
        self.vbox.addWidget(self.button5)
        self.setLayout(self.vbox)
        self.con_obj = ConnectionObject(settings_express)
        self.reporter = Report(self.con_obj.connection, self.con_obj.cursor)
        self.pars_obj = Parser(self.con_obj.connection, self.con_obj.cursor)
        self.loaddelete = LoaderDeleter(self.con_obj.connection, self.con_obj.cursor)
        self.button_path.clicked.connect(self.new_dir)
        self.button.clicked.connect(self.on_clicked)
        self.button2.clicked.connect(self.on_clicked2)
        self.button3.clicked.connect(self.on_clicked3)
        self.button4.clicked.connect(self.on_clicked4)
        self.button5.clicked.connect(self.on_clicked5)
        self.button_load_rrc.clicked.connect(self.rrc_load)
        self.button_load_new.clicked.connect(self.new_load)
        self.button_load_best.clicked.connect(self.best_load)
        self.button_load_all.clicked.connect(self.load_alll)
        self.button_run.clicked.connect(self.parser_start)
        self.button_run_lnk.clicked.connect(self.link_search)

    def load_alll(self):
        self.loaddelete.data_update_to_customers()

    def parser_start(self):
        self.pars_obj.start_price_search_modul()

    def link_search(self):
        self.pars_obj.start_links_search_modul()

    def current_date(self):
        date = datetime.date.today().isoformat()
        return date

    def new_dir(self):
        try:
            os.mkdir(os.path.normpath(os.path.join(self.base_dir, self.today)))
        except:
            pass

    def rrc_load(self):
        self.loaddelete.load_rrc_data()

    def new_load(self):
        self.loaddelete.load_new_data()

    def best_load(self):
        self.loaddelete.load_best_data()

    def on_clicked(self):
        self.button.setDisabled(True)
        time.sleep(1)
        self.reporter.rrc_report(self.today)
        time.sleep(1)
        self.button.setEnabled(True)

    def on_clicked2(self):
        self.button2.setDisabled(True)
        time.sleep(1)
        self.reporter.new_report(self.today)
        time.sleep(1)
        self.button2.setEnabled(True)

    def on_clicked3(self):
        self.button3.setDisabled(True)
        time.sleep(1)
        self.reporter.best_report(self.today)
        time.sleep(1)
        self.button3.setEnabled(True)

    def on_clicked4(self):
        self.button4.setDisabled(True)
        time.sleep(1)
        self.reporter.bad_links_file(self.today)
        time.sleep(1)
        self.button4.setEnabled(True)

    def on_clicked5(self):
        self.button5.setDisabled(True)
        time.sleep(1)
        self.reporter.screenshot_modul()
        time.sleep(1)
        self.button5.setEnabled(True)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.resize(300, 100)
    window.show()
    sys.exit(app.exec_())
