#coding=utf-8
import os
import unittest
from appium import webdriver
from time import sleep

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = 'SM_G9250'
desired_caps['appPackage'] = 'com.ticai.shouyoucai'
desired_caps['appActivity'] = '.Syc3Activity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(10)

driver.find_element_by_id("com.ticai.shouyoucai:id/home_menu_out_btn").click()

driver.find_element_by_id("com.ticai.shouyoucai:id/home_menu_out_btn").click()

#driver.find_element_by_name("1").click()

#driver.find_element_by_name("5").click()
