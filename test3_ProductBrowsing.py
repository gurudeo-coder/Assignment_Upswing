from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.demoblaze.com/")
driver.maximize_window()
driver.implicitly_wait(10)

def test_signup():
   driver.find_element(By.XPATH,'//*[@id="itemc"][3]').click()
   time.sleep(4)

   driver.find_element(By.XPATH,'//*[@class="col-lg-4 col-md-6 mb-4"][2]').click()
   time.sleep(5)

   print('categories navigated successfully')