import selenium
from tier_values import tier_values_UGG, average_tier_value
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
    tier = find.text.replace("\n", " ").replace("Tier", "").replace(" ", "")
    tiers.append(tier)

champion_stats= []
all_tier_values = []
for i in range (len(contents)):
    all_tier_values.append(tier_values_UGG(tiers[i]))   
average_tier = average_tier_value(all_tier_values)
for i in range (len(contents)):
    champion= []
    tier_value = tier_values_UGG(tiers[i])
    champion.append(tiers[i])
    champion.append(tier_value)
    champion.append(tier_value/average_tier) 
    champion_stats.append(champion)

wb=load_workbook('LoLChampions.xlsx')
ws = wb.active
for i in range (len(champion_stats)):
    for j in range (len(champion_stats[i])):
        ws.cell(row=i+2, column=j+11).value = champion_stats[i][j]
wb.save('LoLChampions.xlsx')
wb.close()
