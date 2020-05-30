from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException
import time

contact = "Name in your contact"

text = "Hello!!It is a automatic message send to you using python"

chromedriver="E:/Users/NM/envs/python3/chromedriver_win32/chromedriver"

driver = webdriver.Chrome(chromedriver)
driver.get("https://web.whatsapp.com")

print("Scan QR Code, And then Enter")
print("Logged In")

input_box_search = WebDriverWait(driver,500,ignored_exceptions=(ElementClickInterceptedException)).until(lambda driver: driver.find_element_by_class_name('_2S1VP'))
time.sleep(2)

input_box_search.send_keys(contact)
time.sleep(2)

selected_contact = driver.find_element_by_xpath("//span[@title='"+contact+"']")
selected_contact.click()

inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]'
input_box = driver.find_element_by_xpath(inp_xpath)
time.sleep(2)

for i in range(30):
    input_box.send_keys(text + Keys.ENTER)
time.sleep(2)
driver.quit()
