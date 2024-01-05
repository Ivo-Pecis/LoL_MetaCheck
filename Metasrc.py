from tier_values import tier_values_Metasrc, average_tier_value
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

url = "https://www.metasrc.com/lol/tier-list"
driver.get(url)
time.sleep(2)

find = driver.find_element(By.CLASS_NAME, "css-47sehv")
find.click()
time.sleep(2)  

with open('test.txt') as f:
    contents = f.read().replace('\n', ' ').split(",")
tiers = []
for i in contents:
    find = driver.find_element(By.ID, "nav-search-input")
    find.send_keys(i)
    time.sleep(2)
    keyboard.press(Key.enter)
    time.sleep(2)

    find = driver.find_element(By.CLASS_NAME, "_dxv0e1").text
    tier = find.replace("Tier: \n", "")
    tiers.append(tier)

champion_stats= []
all_tier_values = []
for i in range (len(contents)):
    all_tier_values.append(tier_values_Metasrc(tiers[i]))   
average_tier = average_tier_value(all_tier_values)
for i in range (len(contents)):
    champion= []
    tier_value = tier_values_Metasrc(tiers[i])
    champion.append(tiers[i])
    champion.append(tier_value)
    champion.append(tier_value/average_tier) 
    champion_stats.append(champion)

wb=load_workbook('LoLChampions.xlsx')
ws = wb.active
for i in range (len(champion_stats)):
    for j in range (len(champion_stats[i])):
        ws.cell(row=i+2, column=j+5).value = champion_stats[i][j]
wb.save('LoLChampions.xlsx')
wb.close()

print((champion_stats))