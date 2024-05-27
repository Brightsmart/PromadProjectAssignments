import pytest
from selenium import webdriver
import time
import allure
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType



def test_make_appointment():
    driver = webdriver.Chrome()
    web = driver.get("https://katalon-demo-cura.herokuapp.com/")
    appointment = driver.find_element(By.ID, "btn-make-appointment")
    appointment.click()
    assert driver.current_url != "https://katalon-demo-cura.herokuapp.com/"
    time.sleep(3)
    username = driver.find_element(By.XPATH, "//input[@id='txt-username']")
    password = driver.find_element(By.ID, "txt-password")
    login = driver.find_element(By.ID, "btn-login")
    username.send_keys("John Doe")
    password.send_keys("ThisIsNotAPassword")
    login.click()
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    make_appointment = driver.find_element(By.CSS_SELECTOR, "div[class='col-sm-12 text-center'] h2")
    assert make_appointment.text == "Make Appointment"

    time.sleep(2)
