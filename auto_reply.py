import csv
import random
import smtplib
import time as t

from bs4 import BeautifulSoup as soup
from selenium import webdriver


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

        try:
            msg = last_msg_container[0].span.span.text

            if msg == '':
                msg = last_msg_container[0].span.span.img["alt"]

        except IndexError:
            msg = "Sorry! I can only understand text"
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
            t.sleep(0.01)


def wait_typing(name):
    flag = False
    while True:
        print(name, 'is typing')
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


def wait_new_msgs():
    page = driver.page_source

    while page == driver.page_source:
        t.sleep(5)


def check_new_msgs():
    whatsapp_ps = driver.page_source
    page_soup = soup(whatsapp_ps, "html.parser")

    frnds = []
    left_frame = page_soup.findAll("div", {"class": "X7YrQ"})
    for container in left_frame:
        frnd_container = container.findAll("span", {"class": "P6z4j"})
        if frnd_container:
            name_container = container.find("span", {"class": "_19RFN _1ovWX"})
            name = name_container["title"]

            frnds.append(name)

    return frnds


def convert_data():
    inputs = []
    outputs = []
    with open('replies_data.csv') as data_file:
        reader = csv.reader(data_file)

        flag = True
        for row in reader:
            if flag:
                inputs.append(set(row))
                flag = False

            else:
                outputs.append(row)
                flag = True

    return inputs, outputs


def send_mail(name, msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('abhijeetarabhi@gmail.com', 'vlkwpprmfrdmkrfb')

    subject = 'Unknown message from ' + name
    body = 'Message is ' + msg

    message = f'Subject : {subject}\n\n{body}\n'

    server.sendmail('abhijeetarabhi@whatsapp.com', ['abhijeet_abhi@live.co.uk', 'bandanikhilreddy05@gmail.com'],
                    message)

    print('email sent')


def gen_reply(name, msg, inputs, outputs):
    msg = msg.lower().strip('!').strip('?').strip('.')
    # print("generating reply for ", msg)
    for i in range(len(inputs)):
        if msg in inputs[i]:
            rand_ind = random.randrange(0, len(outputs[i]))
            reply = outputs[i][rand_ind]
            # print('returning reply')
            return reply

    print('Unknown message: ' + msg + ' from: ' + name)
    send_mail(name, msg)
    return


options = webdriver.ChromeOptions();
options.add_argument('--user-data-dir=./User_Data')
driver = webdriver.Chrome('/Users/AR/Documents/Programming/Python/Pycharm/whatsapp_bot/chromedriver',
                          chrome_options=options)
driver.get('https://web.whatsapp.com/')

inputs, outputs = convert_data()

best_frnds = ['Banda', 'Ainesh', 'Dad', 'Mom', 'Indu']

t.sleep(2)
frnds = check_new_msgs()

try:
    while True:

        for name in filter(lambda f: f in best_frnds, frnds):
            frnd = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
            t.sleep(0.05)
            frnd.click()

            t.sleep(0.05)
            wait_typing(name)

            while True:
                try:
                    curr_msgs = read_msgs()
                    break

                except IndexError:
                    t.sleep(1)

            print('Messages: ', curr_msgs)

            if curr_msgs[0] == '':
                t.sleep(1)
                continue

            for msg in curr_msgs[::-1]:
                # print(msg)
                reply = gen_reply(name, msg, inputs, outputs)
                if reply:
                    # print(reply)
                    send_reply(reply)
                    print('Reply : ', reply)

        frnds = check_new_msgs()
        print('hkhlhlhh', frnds)
        if filter(lambda f: f in best_frnds, frnds):
            print('waiting for new messges')
            wait_new_msgs()

except KeyboardInterrupt:
    driver.close()
