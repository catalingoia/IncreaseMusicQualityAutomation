from os import listdir
from os.path import isfile, join
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
print("Introduceti adresa folderului cu muzica:")
adress = input();
files = [f for f in listdir(adress) if isfile(join(adress, f))]

browser = webdriver.Chrome()
converter = webdriver.Chrome()
for f in files:
    browser.get('https://www.youtube.com/results?search_query={}'.format(str(f)))
    browser.implicitly_wait(3)
    browser.find_element_by_id("video-title").click()
    link_to_conv = browser.current_url
    converter.get("https://www.ytmp3.eu")
    converter.find_element_by_xpath("/html/body/center/div[3]/div[2]/input").send_keys(str(link_to_conv))
    converter.find_element_by_xpath("/html/body/center/div[3]/div[2]/button").click()