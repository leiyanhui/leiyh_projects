# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
browser=webdriver.Chrome()
try:


    browser.get("https://www.baidu.com")
    input=browser.find_element_by_id("kw")
    input.send_keys("雷艳辉".decode("utf-8"))
    input.send_keys(Keys.ENTER)
    wait=WebDriverWait(browser,10)
    wait.until(EC.presence_of_element_located((By.ID,"content_left")))
    print(browser.current_url)
    print(browser.get_cookies())
    cookies = browser.get_cookies()
    for cookie in cookies:
        print(cookie)
    print(browser.page_source)
    time.sleep(10)
finally:
    browser.close()