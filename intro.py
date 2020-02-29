from selenium import webdriver                                                  # import selenium webdriver lib
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()   # make driver 
 
driver.get("https://www.youtube.com/")  # url for fetch 

driver.close() 
