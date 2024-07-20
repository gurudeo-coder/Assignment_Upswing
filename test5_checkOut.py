from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def test_positve():
    driver = webdriver.Chrome()
    driver.get('https://www.demoblaze.com/index.html')
    driver.maximize_window()
    time.sleep(3)
    driver.find_element(By.XPATH,'//*[@class="pagination"]//li[2]').click()
    time.sleep(5)
    driver.find_element(By.PARTIAL_LINK_TEXT,'MacBook Pro').click()
    time.sleep(5)
    driver.find_element(By.XPATH,'//*[@class="btn btn-success btn-lg"]').click()
    time.sleep(3)

    popup_l = driver.switch_to.alert
    popup_text = popup_l.text
    print(popup_text)
    popup_l.accept()

    driver.find_element(By.ID, 'cartur').click()
    time.sleep(3)
    print('Product added successfully in cart')
    time.sleep(5)
    # driver.quit()


def test_negative():
    driver = webdriver.Chrome()
    driver.get('https://www.demoblaze.com/index.html')
    driver.maximize_window()
    time.sleep(3)

    driver.find_element(By.ID,'cartur').click()
    print('abc')



