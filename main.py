from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://weblogin.asu.edu/cas/login?")
print(driver.title)

search = driver.find_element(by=By.ID , value ='username')
search.send_keys("Username HERE")

search = driver.find_element(by=By.ID , value ='password')
search.send_keys("Password here")
search.send_keys(Keys.RETURN)
time.sleep(3)

driver.get("https://webapp4.asu.edu/myasu/")
time.sleep(2)

click_btn = pyautogui.locateCenterOnScreen('butt.png')
print(click_btn)
pyautogui.moveTo(click_btn)
time.sleep(1)
pyautogui.click()


time.sleep(15)
link = driver.find_element(by=By.LINK_TEXT , value ="Registration")
link.click()

time.sleep(2)
link = driver.find_element(by=By.LINK_TEXT , value ="Add/Shopping Cart")
link.click()

time.sleep(7)
link = driver.find_element(by=By.LINK_TEXT , value ="Shopping Cart")
link.click()

time.sleep(2)
link = driver.find_element(by=By.LINK_TEXT , value ="2023 Spring")
link.click()


for _ in range(3500):
    time.sleep(3)
    link = driver.find_element(by=By.LINK_TEXT , value ="Enroll")
    link.click()

    time.sleep(1)
    link = driver.find_element(by=By.LINK_TEXT , value ="Yes")
    link.click()

    time.sleep(3)
    link = driver.find_element(by=By.LINK_TEXT , value ="Shopping Cart")
    link.click()