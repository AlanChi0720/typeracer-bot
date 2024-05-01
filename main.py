from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pyautogui
import keyboard

options = Options()

driver = webdriver.Chrome(options=options)

driver.get("https://play.typeracer.com/")

driver.maximize_window()

time.sleep(1)

keyboard.press_and_release('ctrl+alt+o')
time.sleep(1)

# text = driver.find_element(By.CLASS_NAME, "MunejIkN fngyJTfR").text
text = driver.find_element(By.XPATH, "//span[@unselectable='on']").find_element(By.XPATH, "..").text
text = text.split("\n")
print(type(text))
print(text[0])

pyautogui.typewrite(text[0],0.2)

time.sleep(15)
driver.close()

