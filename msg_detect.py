from bs4 import BeautifulSoup as soup
from selenium import webdriver
import time as t

driver = webdriver.Chrome('/Users/AR/Documents/Programming/Python/Pycharm/Whatsapp/chromedriver')
driver.get("http://web.whatsapp.com")
t.sleep(2)

qr_page = driver.page_source
while qr_page == driver.page_source:
    continue

print('QR Scanned\n')
t.sleep(5)

for i in range(10):
    whatsapp_ps = driver.page_source
    page_soup = soup(whatsapp_ps, "html.parser")

    left_frame = page_soup.findAll("div", {"class": "X7YrQ"})
    print('Unread_messages from :')
    for container in left_frame:
        frnd_container = container.findAll("span", {"class": "P6z4j"})
        if frnd_container != []:
            name_container = container.find("span", {"class": "_19RFN _1ovWX"})
            name = name_container["title"]
            
            no_msgs = frnd_container[0].text
            
            print(name, no_msgs)

    t.sleep(5)
