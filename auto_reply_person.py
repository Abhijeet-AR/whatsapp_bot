from bs4 import BeautifulSoup as soup
from selenium import webdriver
import time as t


def read_msgs():
    whatsapp_ps = driver.page_source
    page_soup = soup(whatsapp_ps, "html.parser")

    right_frame = page_soup.findAll("div", {"class": "_3HZor _2rI9W"})[-1]
    messages = right_frame.findAll("div", {"class": "_1ays2"})[-1]

    all_msgs_container = messages.findAll("div", recursive=False)

    msgs = []
    for msg_container in all_msgs_container[::-1]:
        # print('msg_container : ', msg_container["class"])

        if msg_container["class"][0] == "_3Xx0y":
            continue

        if msg_container["class"][1] == "message-out":
            break
        last_msg_container = msg_container.findAll("div", {"class": "_12pGw EopGb"})
        msg = last_msg_container[0].span.span.text
        # print('msg : ', msg)
        msgs.append(msg)

    if len(msgs) == 0:
        return ['']

    return msgs


def send_reply(msg):
    msg_box = driver.find_element_by_class_name('_3u328')
    msg_box.send_keys(msg)

    while True:
        try:
            button = driver.find_element_by_class_name('_3M-N-')
            button.click()
            break

        except:
            t.sleep(1)


def wait_typing():
    flag = False
    while True:
        print('typing')
        whatsapp_ps = driver.page_source
        page_soup = soup(whatsapp_ps, "html.parser")

        typing = page_soup.findAll("span", {"class": "_315-i"})

        try:
            if typing[0].text == 'typing…':
                flag = False

            else:
                if flag:
                    return

                flag = True
                t.sleep(3)

        except IndexError:
            return

        t.sleep(1)


def gen_reply(msg):
    return msg


driver = webdriver.Chrome('/Users/AR/Documents/Programming/Python/Pycharm/Whatsapp/chromedriver')
driver.get("http://web.whatsapp.com")

t.sleep(2)
qr_page = driver.page_source

while qr_page == driver.page_source:
    continue

print('QR Scanned')

name = "Kanchu"
while True:
    try:
        frnd = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
        frnd.click()
        break

    except:
        t.sleep(2)

send_reply('Der? or Not??')
t.sleep(1)

prev_msgs = ['']

# print(prev_msgs)
while True:
    # print('start')
    try:
        curr_msgs = read_msgs()

    except:
        curr_msgs = ["no emojis"]

    print(curr_msgs, prev_msgs)
    if curr_msgs != ['']:
        # print("in")
        wait_typing()
        curr_msgs = read_msgs()
        # print("out")

        print('Message : ', curr_msgs)

        if curr_msgs[0] == '':
            t.sleep(1)
            continue

        for msg in curr_msgs[::-1]:
            reply = gen_reply(msg)
            send_reply(reply)
            print('Reply : ', reply)

        print('waiting for msg...')

    t.sleep(3)
