from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import json


with open("D:\Creative Cloud Files\Creative Cloud Files\Python Projects\Discord Auto Rankup\credentials.json") as jsonFile: #windows users pls specify path to json file
    jsonObject = json.load(jsonFile)
    jsonFile.close()

email = jsonObject['email']
password = jsonObject['password']
delay = int(jsonObject['delay'])
link = jsonObject['channel']

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.notifications": 1
})

browser = webdriver.Chrome(ChromeDriverManager().install(),options=opt)
browser.get(link)


time.sleep(1)
element = browser.find_element_by_name('email')
element.send_keys(email)
time.sleep(1)
element = browser.find_element_by_name('password')
element.send_keys(password)
element.send_keys(Keys.ENTER)
time.sleep(10)
text_element = browser.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div[2]/div/main/form/div/div/div/div/div[3]/div[2]')
n = 373
while True:
    text_element.send_keys('Message number ' + str(n) + ' in pursuit of meaningless internet points')
    text_element.send_keys(Keys.ENTER)
    n += 1
    time.sleep(delay)
