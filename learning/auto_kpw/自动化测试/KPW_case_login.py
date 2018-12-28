import unittest
from appium import webdriver
# from appium_desktop.common import *
from selenium.webdriver.common.by import By
from learning.auto_kpw.自动化测试.PO.base import base_Element
from learning.auto_kpw.自动化测试.PO.login import common_sign_In


class DemoTest(unittest.TestCase):

    # 准备环境
    def setUp(self):
        # 准备环境
        print('before test：Prepare environment.')

        desired_caps = {}

        # 声明是ios还是Android系统
        desired_caps['platformName'] = "Android"
        # Android内核版本号
        desired_caps['platformVersion'] = '8.0'
        # 连接的设备名称
        desired_caps['deviceName'] = 'http://localhost:4723'
        # apk的包名
        desired_caps['appPackage'] = 'com.kpwlottery.app'
        # apk的launcherActivity
        desired_caps['appActivity'] = 'com.cambodia.lt.kpwlottery.activity.SplashActivity'
        # 设置输入法
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'

        '''
        加入这2句话后不仅字母和数字可以输入正常，连中文也可以正确输入。
        这2句话的意思是设置unicode输入法，加完这句话，运行代码后，查看输入法，你原来的输入法被重置了
        '''

        # 建立 session
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    # 执行用例
    def test_case_login(self):
        # driver = self.driver

        # 1.点击图标，跳转至登录页面
        base_Element.common_click(self, By.ID, 'com.kpwlottery.app:id/title_left')

        # 断言：判断页面标题，确定是否进入登录页面
        assert_element = base_Element.common_text(self, By.ID, 'com.kpwlottery.app:id/title_name')
        self.assertEqual(assert_element, '登陆')

        # 2.执行【登录】操作
        common_sign_In.enter_Username(self, 'iOS_Test_001')
        common_sign_In.enter_Password(self, '147258')
        common_sign_In.click_Login(self)

        # 断言：判断页面标题，确定登录成功后是否进入首页
        assert_element = base_Element.common_text(self, By.ID, 'com.kpwlottery.app:id/title_name')
        self.assertEqual(assert_element, 'KPW 彩票')

    # 清理
    def tearDown(self):
        print('after test：Clean up.')
        self.driver.quit()
