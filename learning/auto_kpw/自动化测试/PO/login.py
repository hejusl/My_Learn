from selenium.webdriver.common.by import By
from learning.auto_kpw.自动化测试.PO.base import base_Element


# 在"登录"页面输入用户名、密码,点击【登录】按钮
class common_sign_In:
    # 1.输入用户名
    def enter_Username(self, val):
        base_Element.common_send_keys(self, By.ID, 'com.kpwlottery.app:id/et_user', val)

    # 2.输入密码
    def enter_Password(self, val):
        base_Element.common_send_keys(self, By.ID, 'com.kpwlottery.app:id/et_pwd', val)

    # 3.点击[登录]按钮
    def click_Login(self):
        base_Element.common_click(self, By.ID, 'com.kpwlottery.app:id/btn_login')
