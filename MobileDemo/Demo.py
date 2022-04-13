import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy as By
from selenium.webdriver.support.wait import WebDriverWait

caps={}
caps['platformName'] = "Android"
caps['platformVersion'] = "6.0.1"
caps['deviceName'] = "127.0.0.1:7555"
caps['noReset'] = True
caps['appPackage'] = "com.xueqiu.android"
caps['appActivity'] = ".view.WelcomeActivityAlias"
caps['automationName'] = "Uiautomator2"
appium_driver = "http://127.0.0.1:4723/wd/hub"

driver = webdriver.Remote(appium_driver, caps)
driver.implicitly_wait(20)
driver.find_element(By.XPATH, "//*[@text='股票']").click()
driver.find_element(By.ID, "com.xueqiu.android:id/action_search").click()
driver.find_element(By.ID, "com.xueqiu.android:id/search_input_text").send_keys("alibaba")
driver.find_element(By.XPATH, "//*[text()='阿里巴巴']").click()
