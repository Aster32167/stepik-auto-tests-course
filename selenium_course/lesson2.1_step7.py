from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_xpath ("//img[@id='treasure']")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    option1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
    option1.click()
    option2 = browser.find_element_by_css_selector("[id='robotsRule']")
    option2.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(3)
    browser.quit()
