from selenium import webdriver
import time as t

driver = webdriver.Chrome('/Users/AR/Documents/Programming/Python/Pycharm/Whatsapp/chromedriver')
driver.get('http://web.whatsapp.com')

t.sleep(1)
qr_page = driver.page_source

print('Scan QR')

while driver.page_source == qr_page:
    continue

print('QR Scanned')

name = "Harsha"
while True:
    try:
        frnd = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
        frnd.click()
        break

    except:
        t.sleep(1)


for i in range(109):
    msg_box = driver.find_element_by_class_name('_3u328')
    msg_box.send_keys('Harry')

    button = driver.find_element_by_class_name('_3M-N-')
    button.click()

print('Successful')

