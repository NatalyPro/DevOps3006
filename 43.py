from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///C:/Users/natal/Downloads/ffff/tip_calc/index.html")

driver.find_element(By.ID, 'billamt').click()
driver.find_element(By.ID,'billamt').