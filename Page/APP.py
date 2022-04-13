import os
import time

from appium import webdriver
from Page.BasePage import BasePage
from Page.MainPage import MainPage
class APP(BasePage):
    # __host = "127.0.0.1"
    # __port = "4723"
    __version = "6.0.1"
    __deviceName = "127.0.0.1:7555"
    __noReset = True
    __appPackage = "com.xueqiu.android"
    __appActivity = ".view.WelcomeActivityAlias"
    def start(self):
        if self.driver is None:
            caps={}
            caps['platformName'] = "Android"
            caps['appium:platformVersion'] = self.__version
            caps['appium:deviceName'] = self.__deviceName
            caps['appium:noReset'] = self.__noReset
            caps['unicodeKeyboard'] = True
            caps['resetKeyboard'] = True
            caps['appium:appPackage'] = self.__appPackage
            caps['appium:appActivity'] = self.__appActivity
            # appium_driver = f"http://{self.__host}:{self.__port}/wd/hub"
            appium_driver = f"http://127.0.0.1:4723/wd/hub"
            self.driver = webdriver.Remote(appium_driver, caps)
            self.driver.implicitly_wait(20)
        else:
            self.driver.start_activity(self.__appPackage,self.__appActivity)
            self.driver.implicitly_wait(20)
        return self
    def Main(self):
        return MainPage(self.driver)


# print(app().start().main().go_to_searchpage().search("alibaba").get_price())
