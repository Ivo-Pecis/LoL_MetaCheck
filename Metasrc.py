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
for i in range (len(contents)-1):
    champion= []
    champion.append(tiers[i])
    champion.append(tier_values.tier_values_Metasrc(tiers[i]))
    champion_stats.append(champion)

wb=load_workbook('LoLChampions.xlsx')
ws = wb.active
for i in range (len(champion_stats)):
    for j in range (len(champion_stats[i])):
        ws.cell(row=i+2, column=j+4).value = champion_stats[i][j]
wb.save('LoLChampions.xlsx')
wb.close()