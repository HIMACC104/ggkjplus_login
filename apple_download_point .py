import time
import os
import sys
from selenium import webdriver
#from openpyxl import load_workbook
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#import pandas as pd
from PIL import Image

url_apple_download = 'http://www.ggkjplus.com/admin/#/login'
#chromedriver = './chromedriver.exe'
chromedriver = '/usr/bin/chromedriver.exe'


account_apple = 'your_account_here'
password_apple = 'your_password_here'

options = webdriver.ChromeOptions()
#options.add_argument('--headless')
#options.add_argument('--no-sandbox')

#不載入圖片
options.add_argument('--disable-gpu') 
options.add_argument('blink-settings=imagesEnabled=false')
#options.add_argument('--window-size=1150,1400')
options.add_argument('--enable-features=OverlayScrollbar')

#driver = webdriver.Remote(service.service_url)
driver = webdriver.Chrome(executable_path=chromedriver, options=options)
#driver.execute_script("document.body.style.zoom='0.9'")

#driver.execute_script("document.body.style.transform='scale(0.9)'")
#driver.get('chrome://settings/')
#driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.9);')

driver.implicitly_wait(60)


#driver.find_element(By.ID, "url").click()
#driver.find_element(By.ID, "url").send_keys(url)
#driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/form/div[2]/div/div[1]/input]').click()
driver.get(url_apple_download);
driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/form/div[2]/div/div/input').send_keys(account_apple)
driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/form/div[3]/div/div/input').send_keys(password_apple)
driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/form/button/span').click()


#time.sleep(3)
#driver.get(url_apple_download);
#driver.find_element_by_xpath('/html/body/div/div[3]/div[1]/div[2]/div[1]/div/ul/div[4]/a/li').click()
#driver.find_element_by_xpath('/html/body/div/div[3]/div[1]/div[2]/div[1]/div/ul/div[4]/a/li').click()

time.sleep(3)
driver.get('https://www.ggkjplus.com/admin/#/webpackage');
time.sleep(3)
result = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/section/div/div[1]/ul/li[1]/span/div/span').text
print('剩余付费下载点数 : ',result)

driver.quit()
os.system("pause")
