from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://github.com/shivam007-ss/selenium-/blob/master/intro.py')
time.sleep(5)
driver.close()

