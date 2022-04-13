from appium.webdriver.webdriver import webdriver

class BasePage():
    def __init__(self, driver:webdriver=None):  #指定webdriver
        self.driver = driver
    def find(self, locator, value:str=None):
        if isinstance(locator, tuple):
            return self.driver.find_element(*locator)
        else:
            return self.driver.find_element(locator, value)
