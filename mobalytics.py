import selenium
import tier_values
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
from openpyxl import Workbook as wb, load_workbook 
import time
from pynput.keyboard import Key, Controller

service = Service()
option = webdriver.ChromeOptions()
keyboard = Controller()

driver = webdriver.Chrome(service=service, options=option)

url = "https://www.mobalytics.gg"
driver.get(url)
driver.maximize_window()
time.sleep(2)

find = driver.find_element(By.CLASS_NAME, "fc-button-label")
find.click()
time.sleep(1)

find = driver.find_element(By.CLASS_NAME, "gradient-overlay")
find.click()
time.sleep(2)

with open('test.txt') as f:
    contents = f.read().replace('\n', '').split(",")
tiers = []
for i in contents:
    find = driver.find_element(By.ID, "downshift-1-input")
    if i[0] == " ":
        i = i[1:]
    find.send_keys(i)
    time.sleep(1.5)   
    keyboard.press(Key.enter)
    time.sleep(1)
    find.click()
    find = driver.find_element(By.CLASS_NAME, "m-1mwq4ws")
    tier = find.get_attribute("ALT")
    tiers.append(tier)
    keyboard.press(Key.ctrl)
    keyboard.press("a")
    keyboard.release("a")
    keyboard.release(Key.ctrl)

champion_stats= []
for i in range (len(contents)):
    champion= []
    champion.append(tiers[i])
    champion.append(tier_values.tier_values_mobalytics(tiers[i]))
    champion_stats.append(champion)

wb=load_workbook('LoLChampions.xlsx')
ws = wb.active
for i in range (len(champion_stats)):
    for j in range (len(champion_stats[i])):
        ws.cell(row=i+2, column=j+6).value = champion_stats[i][j]
wb.save('LoLChampions.xlsx')
wb.close()