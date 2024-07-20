from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://www.demoblaze.com/index.html')
time.sleep(3)
def test_AddToCart():
    driver.find_element(By.XPATH,'//*[@class="pagination"]//li[2]').click()
    time.sleep(5)
    driver.find_element(By.PARTIAL_LINK_TEXT,'MacBook Pro').click()
    time.sleep(5)
    driver.find_element(By.XPATH,'//*[@class="btn btn-success btn-lg"]').click()
    time.sleep(3)

    print("Item is added sucessfully")
