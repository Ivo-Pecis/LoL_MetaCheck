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

url = "https://www.u.gg"
driver.get(url)
time.sleep(2)

find = driver.find_element(By.CLASS_NAME, "css-47sehv")
find.click()
time.sleep(2)

find = driver.find_element(By.CLASS_NAME, "autosuggest-container")
temp = find.find_element(By.ID, "super-search-bar")
temp.send_keys("Aatrox")
time.sleep(7)
keyboard.press(Key.enter)
keyboard.release(Key.enter) 
time.sleep(3)

with open('test.txt') as f:
    contents = f.read().replace('\n', '').split(",")
tiers = []
for i in contents:
    find = driver.find_element(By.CLASS_NAME, "react-autosuggest__container")
    find.click()
    keyboard.press(Key.ctrl)
    keyboard.press("a")
    keyboard.release("a")
    keyboard.release(Key.ctrl) 
    keyboard.type(i)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(3)
    find = driver.find_element(By.CLASS_NAME, "champion-tier.media-query.media-query_MOBILE_LARGE__DESKTOP_LARGE")
    tier = find.text.replace("\n", " ").replace("Tier", "")
    tiers.append(tier)

champion_stats= []
for i in range (len(contents)):
    champion= []
    champion.append(tiers[i])
    champion.append(tier_values.tier_values_UGG(tiers[i]))
    champion_stats.append(champion)

wb=load_workbook('LoLChampions.xlsx')
ws = wb.active
for i in range (len(champion_stats)):
    for j in range (len(champion_stats[i])):
        ws.cell(row=i+2, column=j+8).value = champion_stats[i][j]
wb.save('LoLChampions.xlsx')
wb.close()

input()