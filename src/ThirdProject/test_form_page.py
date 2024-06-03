import pytest
from selenium import webdriver
import time
import allure
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType

@pytest.mark.smoke
@allure.title("Error message verification")
@allure.description("An error Message is to pop up when username is blank")
def test_task():
    driver = webdriver.Chrome()
    web_page = driver.get("https://cdpn.io/AbdullahSajjad/fullpage/LYGVRgK?anon=true&view=fullpage")
    time.sleep(5)
    driver.switch_to.frame(driver.find_element(By.ID,"result"))
    Email = driver.find_element(By.ID, "email")
    Password = driver.find_element(By.XPATH, "//input[@id='password']")
    Con_Password = driver.find_element(By.XPATH, "//input[@id='password2']")
    Submit = driver.find_element(By.XPATH, "//button[normalize-space()='Submit']")
    Email.send_keys("jijigy@gmail.com")
    Password.send_keys("1234me1")
    Con_Password.send_keys("1234me1")
    Submit.click()
    time.sleep(5)
    error_message = driver.find_element(By.XPATH, "//small[normalize-space()='Username must be at least 3 characters']")
    assert error_message.text == "Username must be at least 3 characters"
    allure.attach(driver.get_screenshot_as_png(),name="Error Message",attachment_type=AttachmentType.PNG)

    driver.quit()