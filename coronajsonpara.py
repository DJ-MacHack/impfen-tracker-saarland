from selenium import webdriver
from datetime import datetime
import time
import re
import _thread

path = 'C:\chromedriver.exe'
# create nstance of webdriver
# google url
url0 = 'https://impfen-saarland.de/service/api/left_over/availabilities.json?event_category_id=85040'
url1 = 'https://impfen-saarland.de/service/api/left_over/availabilities.json?event_category_id=85041'
url2 = 'https://impfen-saarland.de/service/api/left_over/availabilities.json?event_category_id=85042'
url3 = 'https://impfen-saarland.de/service/api/left_over/availabilities.json?event_category_id=87534'
url4 = 'https://impfen-saarland.de/service/api/left_over/availabilities.json?event_category_id=87534-night'

def brute_entries(url, ort):
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
            print(ort)
            print(re.findall(r'\[.+\]', html))
            print(datetime.now().strftime("%H:%M:%S"))
        #driver.close()
        time.sleep(0.5)

try:
    _thread.start_new_thread(brute_entries, (url0, "Neunkirchen"))
    _thread.start_new_thread(brute_entries, (url1, "Saarlouis"))
    _thread.start_new_thread(brute_entries, (url2, "Saarbrücken"))
    _thread.start_new_thread(brute_entries, (url3, "Lebach"))
    _thread.start_new_thread(brute_entries, (url4, "Lebach - Nacht"))
except: 
    print("Error")
    
while 1:
    pass