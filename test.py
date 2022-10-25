from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep
import pyautogui
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://testlink.org/')
title = driver.title
assert title == 'TestLink'

donate_button = driver.find_element(By.XPATH, "/html/body/div/div[3]/div/form/input[9]")
print(donate_button)

name_donate = donate_button.get_attribute('name')

print(name_donate)

assert name_donate == 'submit'

github_element = driver.find_element(By.XPATH, "/html/body/div/div[3]/div/a[3]")
github_element.click()

github_url = driver.current_url

assert github_url == 'https://github.com/TestLinkOpenSourceTRMS/testlink-code/tree/testlink_1_9_20_fixed/'

driver.quit()
