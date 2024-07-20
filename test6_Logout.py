from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Give new Passwrd else It will Fail

def test_Logout():
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
    time.sleep(3)
    # print('sucessfully login')
    #
    driver.find_element(By.ID,'logout2').click()
    print('Successfully log out.')
    time.sleep(3)
    #
