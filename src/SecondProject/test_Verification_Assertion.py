import pytest
from selenium import webdriver
import time
import allure
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType


def test_verify_trial_assertion():
    driver = webdriver.Chrome()
    web = driver.get("https://www.idrive360.com/enterprise/login")
    #time.sleep()
    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    login = driver.find_element(By.XPATH,"//button[@id='frm-btn']")
    username.send_keys("augtest_040823@idrive.com")
    password.send_keys("123456")
    login.click()
    time.sleep(25)
    assert driver.current_url != web
    free_trial = driver.find_element(By.CSS_SELECTOR, ".id-card-title")
    assert free_trial.text == "Your free trial has expired"
    allure.attach(driver.get_screenshot_as_png(),name="Warning message", attachment_type=AttachmentType.PNG)
