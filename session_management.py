from selenium import webdriver
import time as t

options = webdriver.ChromeOptions();
options.add_argument('--user-data-dir=./User_Data')
driver = webdriver.Chrome('/Users/AR/Documents/Programming/Python/Pycharm/whatsapp_bot/chromedriver', chrome_options=options)
driver.get('https://web.whatsapp.com/')

t.sleep(2)
qr_page = driver.page_source

while qr_page == driver.page_source:
    continue

print('QR Scanned')

t.sleep(20)
driver.close()