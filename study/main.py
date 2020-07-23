# encoding = utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.maximize_window()

# while True:
driver.get("http://hd.huangxiu1.com/huodong/2020anniversary/")

driver.execute_script("alert(JSON.stringify(f))")