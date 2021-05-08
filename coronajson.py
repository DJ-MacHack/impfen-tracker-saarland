from selenium import webdriver
from datetime import datetime
import time
import re
# path to chromedriver.exe 
path = 'C:\chromedriver.exe'
# create nstance of webdriver
# google url
url = 'https://impfen-saarland.de/service/api/left_over/availabilities.json?event_category_id=85040'
url1 = 'https://impfen-saarland.de/service/api/left_over/availabilities.json?event_category_id=85041'
url2 = 'https://impfen-saarland.de/service/api/left_over/availabilities.json?event_category_id=85042'
url3 = 'https://impfen-saarland.de/service/api/left_over/availabilities.json?event_category_id=87534'
url4 = 'https://impfen-saarland.de/service/api/left_over/availabilities.json?event_category_id=87534-night'
# Code to open a specific url
driver = webdriver.Chrome(path)
size = 522
while 1:
    #driver = webdriver.Chrome(path)
    driver.get(url)
    html = driver.page_source
    time.sleep(0.2)
    #print(html)
    if len(html) > size:
        print("Neunkirchen")
        print(re.findall(r'\[.+\]', html))
        print(datetime.now().strftime("%H:%M:%S"))
    #driver.close()
    time.sleep(0.5)
    #driver = webdriver.Chrome(path)
    driver.get(url1)
    html = driver.page_source
    time.sleep(0.2)
    #print(html)
    if len(html) > size:
        print("Saalouis")
        print(re.findall(r'\[.+\]', html))
        print(datetime.now().strftime("%H:%M:%S"))
    #driver.close()
    time.sleep(0.5)
    #driver = webdriver.Chrome(path)
    driver.get(url2)
    html = driver.page_source
    time.sleep(0.2)
    #print(html)
    if len(html) > size:
        print("Saarbrücken")
        print(re.findall(r'\[.+\]', html))
        print(datetime.now().strftime("%H:%M:%S"))
    #driver.close()
    time.sleep(0.5)
    driver.get(url3)
    html = driver.page_source
    time.sleep(0.2)
    #print(html)
    if len(html) > size:
        print("Lebach")
        print(re.findall(r'\[.+\]', html))
        print(datetime.now().strftime("%H:%M:%S"))
    #driver.close()
    time.sleep(0.5)
    driver.get(url4)
    html = driver.page_source
    time.sleep(0.2)
    #print(html)
    if len(html) > size:
        print("Lebach Nacht")
        print(re.findall(r'\[.+\]', html))
        print(datetime.now().strftime("%H:%M:%S"))
    #driver.close()
    time.sleep(0.5)