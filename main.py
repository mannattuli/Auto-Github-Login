from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


username = 'username'
password = 'password'

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://github.com/login")

usernameFill = driver.find_element_by_id("login_field")
usernameFill.send_keys(username)


passwordFill = driver.find_element_by_id("password")
passwordFill.send_keys(password)

loginClick = driver.find_element_by_name("commit")
loginClick.click()