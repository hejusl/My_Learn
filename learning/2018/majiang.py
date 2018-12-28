# !/usr/local/bin/python3
# coding=utf-8
'''
计算器-手机自动化  -加法  3+6=9?
'''
from appium import webdriver
# 1>获取手机信息--存储到字典中
desired_caps = {}
# a.平台名称
desired_caps['platformName'] = 'Android'
# b.android版本
desired_caps['platformVersion'] = '8.0.0'
# c.设备名称-- adb devices
desired_caps['deviceName'] = '263b5d2e'
# d.包名
# 获取包名: uiautomatorviewer
desired_caps['appPackage'] = 'com.majiang.jincai.android'
# e. Activity名称
# CatLog工具安装: dos进入c盘--adb install CatLog.apk
desired_caps['appActivity'] = '.hwyxapp'
# 2>连接appium启动app,将手机信息导入;http://127.0.0.1:4723 是appium的地址和端口号，可在appium设置中查看。/wd/hub是appium规定的后缀，记住就好。。
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# 3>定位  3+6=9?
# 3  resource-id-->对应id方法
driver.find_element_by_id("com.miui.calculator:id/btn_3_s").click()
# + 碰到中文前面加小u   content-desc-->对应的name方法
driver.find_element_by_id("com.miui.calculator:id/btn_plus_s").click()
# 6 text-->对应的为name方法
driver.find_element_by_id("com.miui.calculator:id/btn_6_s").click()
# =
driver.find_element_by_id("com.miui.calculator:id/btn_equal_s").click()

# 获取实际结果 class --  class_name      text方法获取元素的内容,后面没有小括号
# result = str(driver.find_element_by_class_name("android.widget.HorizontalScrollView").text)
result = str(driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView[3]/android.widget.LinearLayout/android.widget.TextView[2]").text)


print(result)

# 由于我的手机计算器结果框会输出 3+6=9，所以做一下处理，只取出等号=后面的数字
#result = result.split('=', 1)

# 比对实际结果与预期结果,得出结论
if int(result) == 9:
    print("测试通过")
else:
    print("测试失败")

# 关闭计算器
driver.quit()