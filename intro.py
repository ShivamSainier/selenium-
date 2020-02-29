from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.youtube.com/')
print(driver.title)
print(driver.current_url)
time.sleep(5)
driver.get('https://mail.google.com/mail/u/0/#inbox')
print(driver.title)
print(driver.current_url)
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.close()

