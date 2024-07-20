from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_signup():
    driver = webdriver.Chrome()
    driver.get("https://www.demoblaze.com/")

    driver.maximize_window()
    driver.implicitly_wait(10)
    sign_in_button = driver.find_element(By.ID, "login2")
    sign_in_button.click()
    time.sleep(2)
    username_field = driver.find_element(By.ID, "loginusername")
    password_field = driver.find_element(By.ID, "loginpassword")

    username_field.send_keys("ekantik")
    password_field.send_keys("123456")
    submit_button = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
    submit_button.click()
    print ('sucessfully login')

def test_negative():
    driver = webdriver.Chrome()
    driver.get("https://www.demoblaze.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    sign_in_button = driver.find_element(By.ID, "login2")
    sign_in_button.click()
    time.sleep(2)
    username_field = driver.find_element(By.ID, "loginusername")
    password_field = driver.find_element(By.ID, "loginpassword")

    username_field.send_keys("ekantik")
    password_field.send_keys("123457")
    submit_button = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
    submit_button.click()
    time.sleep(5)

    popup_l = driver.switch_to.alert
    popup_text = popup_l.text
    print(popup_text)
    excepted='Wrong password.'

    time.sleep(5)
    popup_l.accept()

    assert popup_text==excepted

    # driver.find_element(By.ID, 'cartur').click()
    # time.sleep(3)
    # print('Product added successfully in cart')
    # time.sleep(5)
    # driver.quit()

#
#
#
#
#











#
# popup_l = driver.switch_to.alert
#     popup_text = popup_l.text
#     print(popup_text)
#     popup_l.accept()
#
#     driver.find_element(By.ID, 'cartur').click()
#     time.sleep(3)
#     print('Product added successfully in cart')
#     time.sleep(5)
#     # driver.quit()
