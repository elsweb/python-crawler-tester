import time
import os
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install()) 
options = webdriver.ChromeOptions()

options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
options.add_experimental_option("useAutomationExtension", False) 

driver = webdriver.Chrome(service=service, options=options)
action = webdriver.ActionChains(driver)

driver.maximize_window()

#driver.get('https://google.com.br') 
#driver.get('https://mangaschan.net') 
driver.get('https://nowsecure.nl')

time.sleep(300)

driver.close()