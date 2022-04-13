import os
import sys
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy as By
from selenium.webdriver.support.wait import WebDriverWait

appPackage = "com.xueqiu.android"
appActivity = ".view.WelcomeActivityAlias"
# 连接真机
caps={
  "platformName": "Android",
  "appium:platformVersion": "6.0.1",
  "appium:deviceName": "127.0.0.1:7555",
  "appium:noReset": True,
  "appium:appPackage": appPackage,
  "appium:appActivity": appActivity,
  "appium:automationName": "Uiautomator2"
  # 如果需要切换到小程序（属于移动端H5[看不到链接]/webview[有链接]）
  # 需要在初始化界面加入chromedriverExecutable:下载对应版本的Google安装到项目的根目录，windows一定要加后缀".exe"
  # "appium:chromedriverExecutable": "Google驱动地址"
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',caps)
driver.implicitly_wait(10)
# # 以下操作前置条件：app已经打开置后台状态:
# # 1.重新启动app
# os.system("adb shell input keyevent 3")
# time.sleep(2)
# # 2.启动APP页面
# driver.launch_app()
# driver.start_activity(appPackage,appActivity)
# # 3.关闭当前页面，注意quit只适用于web端
# driver.close_app()
# # 4.切换进入H5/webview页面,注意初始化添加chromedriverExecutable
# driver.switch_to.context("com.xueqiu.android")
# # 5.退出H5页面
# driver.switch_to.default_content()
# print(driver.current_package)#打印获取到的 当前界面的程序包名
# # 全局变量,获取页面的高度和宽度，可以等比缩小或放大
# 适用于兼容性测试，或者找不到元素的时候，调整大小，用于封装函数
# global x, y
# x=driver.get_window_size()['width']
# x*0.8
# y=driver.get_window_size()['height']
# y*0.8
# 滑动页面
# "adb shell input swipe x1 y1 x2 y2 time"
# time.sleep(10)
# driver.swipe(1000,900,100,1200,1000)
# TouchAction(driver).move_to(100,100).click()


driver.find_element(By.ID,"com.xueqiu.android:id/profile_image").click()
driver.find_element(By.CSS_SELECTOR,"*[text='手机号']").click()

driver.find_element(By.ID,"com.xueqiu.android:id/register_phone_number").send_keys("15571595185")
driver.find_element(By.ID,"com.xueqiu.android:id/register_code").send_keys("1234")
driver.find_element(By.ID,"com.xueqiu.android:id/button_next").click()
# 用于生成xpath定位 相当于 "//*[@text='请先勾选并同意相关协议']"
toast_message = "请先勾选并同意相关协议"
message ='//*[@text=\'{}\']'.format(toast_message)

# 获取toast提示框内容
toast_element = WebDriverWait(driver,10).until(lambda x:x.find_element_by_xpath(message))
print(toast_element.text)
assert toast_element.text == "请先勾选并同意相关协议"