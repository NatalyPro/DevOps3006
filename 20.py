from time import sleep

from selenium import webdriver
my_driver = webdriver.Chrome("C:/Users/natal/chromedriver.exe")
my_driver.get("file:///C:/Users/natal/Downloads/ffff/tip_calc/index.html")
billamt = my_driver.find_element(by="id", value="billamt")
billamt.send_keys("100")


