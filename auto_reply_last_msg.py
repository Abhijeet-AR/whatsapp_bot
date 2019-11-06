from bs4 import BeautifulSoup as soup
from selenium import webdriver
import time as t


def read_msg():
    whatsapp_ps = driver.page_source
    page_soup = soup(whatsapp_ps, "html.parser")

    right_frame = page_soup.findAll("div", {"class": "_3HZor _2rI9W"})[-1]
    messages = right_frame.findAll("div", {"class": "_1ays2"})[-1]

    last_msgs_day_container = messages.findAll("div", {"class": "FTBzM message-in"})
    last_msg_container = last_msgs_day_container[-1].findAll("div", {"class": "_12pGw EopGb"})
    last_msg = last_msg_container[0].span.span.text

    return last_msg


def send_reply(msg):
    msg_box = driver.find_element_by_class_name('_3u328')
    msg_box.send_keys(msg)

    button = driver.find_element_by_class_name('_3M-N-')
    button.click()


def gen_reply(msg):
    return msg


driver = webdriver.Chrome('/Users/AR/Documents/Programming/Python/Pycharm/Whatsapp/chromedriver')
driver.get("http://web.whatsapp.com")

t.sleep(2)
qr_page = driver.page_source

while qr_page == driver.page_source:
    continue

print('QR Scanned')

name = "Banda"
while True:
    try:
        frnd = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
        frnd.click()
        break

    except:
        t.sleep(1)

send_reply('hi')
t.sleep(1)

while True:
    try:
        prev_msg = read_msg()
        break

    except:
        t.sleep(1)

while True:
    try:
        last_msg = read_msg()

    except:
        last_msg = "no emojis"

    if prev_msg != last_msg:
        print('Message : ', last_msg)

        reply = gen_reply(last_msg)
        send_reply(reply)

        print('Reply : ', reply)
        prev_msg = last_msg
        print('waiting for msg...')

    t.sleep(1)
