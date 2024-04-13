from auto_download_undetected_chromedriver import download_undetected_chromedriver
folder_path = "F:\\Playground\\python\\python-crawler-tester\\"
chromedriver_path = download_undetected_chromedriver(
	folder_path, 
	undetected=True, 
	arm=False, 
	force_update=True
)


import time
import undetected_chromedriver as uc
from selenium import webdriver

options = webdriver.ChromeOptions() 
driver = uc.Chrome(
	driver_executable_path= chromedriver_path
)
driver.get('https://mangaschan.net')
#driver.get('https://nowsecure.nl')
#driver.save_screenshot('nowsecure.png')
time.sleep(300)