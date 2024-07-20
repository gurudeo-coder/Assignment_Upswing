from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Give new Passwrd else It will Fail

def test_signup():
    driver = webdriver.Chrome()

    driver.get("https://www.demoblaze.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    sign_in_button = driver.find_element(By.ID, "signin2")
    sign_in_button.click()

    username_field = driver.find_element(By.ID, "sign-username")
    password_field = driver.find_element(By.ID, "sign-password")

    username_field.send_keys("Shwet7a")
    time.sleep(2)
    password_field.send_keys("9876546")
    time.sleep(2)

    submit_button = driver.find_element(By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]')
    submit_button.click()
    time.sleep(3)

    popup = driver.switch_to.alert
    popup_text = popup.text
    print(f"Alert text: {popup_text}")

    expected_text = "Sign up successful."
    assert popup_text == expected_text
    print("succesful")

    popup.accept()
    # driver.quit()

def test_SignUpNegative():
        driver = webdriver.Chrome()
        driver.get("https://www.demoblaze.com/")
        driver.maximize_window()
        driver.implicitly_wait(10)
        sign_in_button = driver.find_element(By.ID, "signin2")
        sign_in_button.click()

        username_field = driver.find_element(By.ID, "sign-username")
        password_field = driver.find_element(By.ID, "sign-password")

        username_field.send_keys("Shwet7a")
        time.sleep(2)
        password_field.send_keys("9876546")
        time.sleep(2)

        submit_button = driver.find_element(By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]')
        submit_button.click()
        time.sleep(3)

        popup = driver.switch_to.alert
        popup_text = popup.text
        print(popup_text)
        time.sleep(3)

        expected_text = "This user already exist."
        assert popup_text == expected_text
        print("Alredy exist")
        time.sleep(3)

        popup.accept()
        # driver.quit()






