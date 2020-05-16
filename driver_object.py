from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities as DC
import os


class FastDriver(object):
    def __init__(self, driver_number='one'):
        self.driver_file_name = 'chromedriver.exe'
        self.driver_number = driver_number
        self.driver_path = self.set_driver_path()
        self.driver_options = self.set_driver_options()
        self.desired_capabilities = self.set_desired_capabilities()
        self.driver = self.launch_driver()

    def set_driver_path(self):
        path = os.path.normpath(os.path.join(os.getcwd(), 'drivers', self.driver_number, self.driver_file_name))
        return path

    def set_driver_options(self):
        options = webdriver.ChromeOptions()
        return options

    def set_desired_capabilities(self):
        capabilities = DC().CHROME
        capabilities['pageLoadStrategy'] = 'none'
        return capabilities

    def launch_driver(self):
        driver = webdriver.Chrome(executable_path=self.driver_path,
                                  chrome_options=self.driver_options,
                                  desired_capabilities=self.desired_capabilities)
        return driver

    def quit_driver(self):
        self.driver.quit()


class LongDriver(object):
    def __init__(self, driver_number='one'):
        self.driver_file_name = 'chromedriver.exe'
        self.driver_number = driver_number
        self.driver_path = self.set_driver_path()
        self.driver_options = self.set_driver_options()
        self.driver = self.launch_driver()

    def set_driver_path(self):
        path = os.path.normpath(os.path.join(os.getcwd(), 'drivers', self.driver_number, self.driver_file_name))
        return path

    def set_driver_options(self):
        options = webdriver.ChromeOptions()
        return options

    def launch_driver(self):
        driver = webdriver.Chrome(executable_path=self.driver_path,
                                  chrome_options=self.driver_options,)
        return driver

    def quit_driver(self):
        self.driver.quit()

