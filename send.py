from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_eight_components():
    driver = webdriver.Chrome()

    driver.get("http://127.0.0.1:5500/")

    # title = driver.title
    # assert title == "Web form"

    driver.implicitly_wait(2.5)

    text_box = driver.find_element(by=By.NAME, value="username")
    time.sleep(2) # Add delay
    text_box.send_keys("eyal")
    
    pwd = driver.find_element(by=By.NAME, value="password")
   
    pwd.send_keys("123")
    time.sleep(2) # Add delay
    submit_button = driver.find_element(by=By.NAME, value="Login")

    driver.implicitly_wait(2.5)
    submit_button.click()
    time.sleep(12) # Add delay
    message = driver.find_element(by=By.ID, value="message")
    # value = message.text
    # assert value == "Received!"
    # print(message.text)
    # driver.quit()


test_eight_components()