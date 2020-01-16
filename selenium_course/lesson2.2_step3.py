from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    a = int(browser.find_element_by_xpath ("//span[@id='num1']").text) + int(browser.find_element_by_xpath("//span[@id='num2']").text)

    select = Select(browser.find_element_by_class_name("custom-select"))
    select.select_by_visible_text(str(a))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(3)
    browser.quit()
