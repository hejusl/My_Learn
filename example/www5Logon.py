#!/usr/bin/env python
#coding=utf-8

from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time
import os
import random

# 定义订单列表
order_list = []

# o打开火狐浏览器
browser = webdriver.Firefox()

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

#判断登录成功
print ("您好，",browser.find_element_by_xpath("//div[@class='no_login']/font").text)

# switch to main handle
browser.switch_to_window(handle)

# opne ssq page
browser.find_element_by_xpath("//a[contains(@href,'/buy/index.do?lotteryid=101')]").click()

#termselect = browser.find_element_by_id("issue_select")
#termselect.find_element_by_xpath("//option[contains(@value,'20148508')]").click()

# select term 
browser.find_element_by_id("issue_select").find_elements_by_tag_name("option")[0].click()

#browser.find_element_by_xpath("//select[@id='issue_select']/option[0]").click()

# random oen titcket
browser.find_element_by_xpath("//a[contains(@onclick,'lot.ball_rand(1); return false')]").click()

# ========选号开始==========

browser.switch_to_frame("lottery_frame")

print ("您的号码是：")
# 01,02,03,04,05,06#01
# 选红球
redBall = browser.find_elements_by_xpath("//table[@id='hall_2s_select_ball_red']/tbody/tr/td/div")
for i in range(6):
    redBall[i].click()
    print (i+1,end=" ")

# 选篮球
blueBall = browser.find_elements_by_xpath("//table[@id='hall_2s_select_ball_blue']/tbody/tr/td/div")
for j in range(1):
    blueBall[j].click()
    print ("#",j+1)

browser.switch_to_window(handle)

# 添加到选号列表
browser.find_element_by_xpath("//*[contains(@onclick,'lot.insert();')]").click()

browser.switch_to_frame("lottery_frame")
# 手动随机

for i in (random.sample(range(33), 6)):
    redBall[i].click()
    print(i+1,end=" ")

j = random.randrange(0, 16)
blueBall[j].click()
print ("#",j+1)

browser.switch_to_window(handle)

# 添加到选号列表
browser.find_element_by_xpath("//*[contains(@onclick,'lot.insert();')]").click()

#设置倍数
browser.find_element_by_id("order_timesby").clear()
browser.find_element_by_id("order_timesby").send_keys("3")

# 点击提交
browser.find_element_by_xpath("//*[contains(@src,'/tpl/default/buy/images/submit_button_stop.png')]").click()

# 确认投注
browser.switch_to_frame("_x_open_frame_")
browser.find_element_by_xpath("//*[contains(@src,'/tpl/default/buy/images/btn_confirm.png')]").click()

# 打印投注成功：恭喜！您的订单已经提交成功！
print (browser.find_element_by_xpath("//div[@class='order_confirm_content']/p/span").text)
# ========选号结束========

# 取得订单地址
order = browser.find_element_by_xpath("//a[contains(@href,'/cp/dgdetail_')]")
order_url = order.get_attribute("href")
print (order_url)

order_list.append(re.sub("\D", "", order_url)

# 关闭投注成功提示页

#browser.find_element_by_xpath("//*[contains(@class,'button_grey_60x24')]").click()

# 打开个人中心的投注记录
#browser.get(url)
#browser.switch_to_window(handle)
#browser.switch_to_frame("topLoginiframe")
#browser.find_element_by_xpath("//a[@target='_top']").click()



#browser.get_log
#time.sleep(3)
#browser.close()

