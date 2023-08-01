from selenium import webdriver
from selenium.webdriver.common.by import By


def test_eight_components():
    driver = webdriver.Chrome()

    driver.get("http://localhost:3000/")

    # title = driver.title
    # assert title == "Web form"

    driver.implicitly_wait(2.5)

    text_box = driver.find_element(by=By.NAME, value="user")
    text_box.send_keys("eyal")
    pwd = driver.find_element(by=By.NAME, value="pwd")
    pwd.send_keys("123")
    driver.implicitly_wait(2.5)
    submit_button = driver.find_element(by=By.NAME, value="Submit")

    driver.implicitly_wait(2.5)
    submit_button.click()
    driver.implicitly_wait(2.5)
    message = driver.find_element(by=By.ID, value="message")
    # value = message.text
    # assert value == "Received!"
    # print(message.text)
    # driver.quit()


test_eight_components()