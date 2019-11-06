from bs4 import BeautifulSoup as soup
from selenium import webdriver
import time as t

driver = webdriver.Chrome('/Users/AR/Documents/Programming/Python/Pycharm/Whatsapp/chromedriver')
driver.get("http://web.whatsapp.com")

t.sleep(2)
qr_page = driver.page_source

while qr_page == driver.page_source:
    continue

print('QR Scanned')

name = "Dad"
while True:
    try:
        frnd = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
        frnd.click()
        break

    except:
        t.sleep(1)

whatsapp_ps = driver.page_source
page_soup = soup(whatsapp_ps, "html.parser")

right_frame = page_soup.findAll("div", {"class":"_3HZor _2rI9W"})[-1]
messages = right_frame.findAll("div", {"class" : "_1ays2"})[-1]


all_msgs_container = messages.findAll("div", recursive=False)
for msg_container in all_msgs_container[::-1]:
    if msg_container["class"][1] == "message-out":
        break
    last_msg_container = msg_container.findAll("div", {"class": "_12pGw EopGb"})
    msg = last_msg_container[0].span.span.text
    print('msg : ', msg)




