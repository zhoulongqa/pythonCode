#encoding=utf-8
from util.log import *
from selenium import webdriver
import time

info("开始测试:")
driver=webdriver.Firefox(executable_path="c:\\geckodriver")
info(u"访问126首页")
driver.get("http://mial.126.com")

time.sleep(2)
info(u"断言是否有登录2个字")
assert u"登录" in driver.page_source

driver.quit()
info("结束测试:")

