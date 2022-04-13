import time
from appium.webdriver.common.mobileby import MobileBy
from Page.BasePage import BasePage
from Page.searchPage import searchPage
from Page.MyPage import myPage
class MainPage(BasePage):
    def go_to_searchpage(self):
        value = "//*/android.widget.ViewFlipper/android.widget.LinearLayout/android.widget.TextView"
        self.find(MobileBy.XPATH, value).click()
        time.sleep(2)
        return searchPage(self.driver)
    def go_to_mypage(self):
        value = ""
        self.find(MobileBy.XPATH, value).click()
        return myPage(self.driver)