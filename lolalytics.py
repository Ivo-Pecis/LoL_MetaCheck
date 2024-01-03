import selenium
import tier_values
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
from openpyxl import Workbook as wb, load_workbook 
import time

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url = "https://www.lolalytics.com"
driver.get(url)
time.sleep(2)

find = driver.find_element(By.CLASS_NAME, "ncmp__btn")
find.click()
time.sleep(3)

find = driver.find_element(By.CLASS_NAME, "ncmp__btn.ncmp__btn-danger")
find.click()
time.sleep(2)

with open('test.txt') as f:
    contents = f.read().replace('\n', ' ').split(",")
tiers = []
for i in contents:
    find=driver.find_element(By.CLASS_NAME, "SearchBar_search__BJeOt")
    find.click()

    keyboard = Controller()
    keyboard.type(i)
    keyboard.press(Key.enter)
    time.sleep(1)

    find=driver.find_element(By.CLASS_NAME, "CircleBig_wrapper__GgAW5")
    tier = find.find_element(By.CLASS_NAME, "CircleBig_tier__8AcED").text
    tiers.append(tier)
champion_stats= []
for i in range (len(contents)-1):
    champion= []
    champion.append(contents[i]) 
    champion.append(tiers[i])
    champion.append(tier_values.tier_values_LoLalytics(tiers[i]))
    champion_stats.append(champion)

wb=load_workbook('LoLChampions.xlsx')
ws = wb.active
for i in range (len(champion_stats)):
    for j in range (len(champion_stats[i])):
        ws.cell(row=i+2, column=j+1).value = champion_stats[i][j]
wb.save('LoLChampions.xlsx')
wb.close()