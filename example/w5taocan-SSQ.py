#!/usr/bin/env python
# coding=utf-8

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
import os
import random

# 定义订单列表
order_list = []

# o打开火狐浏览器
browser = webdriver.Chrome()

# 设置打开地址
url = ("http://www5.huacai.com")

# 打开首页
browser.get(url)

# 智能等待
browser.implicitly_wait(30)

# set window handle
handle = browser.current_window_handle

# switch to logon frame
browser.switch_to_frame("topLoginiframe")

# input user name
browser.find_element_by_id("account").send_keys("hfliu")

# input password
browser.find_element_by_id("password").send_keys("123123")

# click logon
browser.find_element_by_id("imageField").click()

# 判断登录成功
print ("您好，",browser.find_element_by_xpath("//div[@class='no_login']/font").text)

# switch to main handle
browser.switch_to_window(handle)

# opne ssq page
browser.find_element_by_link_text("双色球").click()

###打开套餐页面
browser.find_element_by_id("xtab_play3").click()

browser.window_handles()
