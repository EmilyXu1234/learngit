from Page.BasePage import BasePage
from appium.webdriver.common.mobileby import MobileBy
class searchPage(BasePage):
    def search(self, revtext=None):
        self.find(MobileBy.ID, "search_input_text").send_keys(revtext)
        self.find(MobileBy.ID, "name").click()
        return self
    def get_price(self):

        return float(self.find(MobileBy.XPATH, "//*/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.TextView[1]").text)