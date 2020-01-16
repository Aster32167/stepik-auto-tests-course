from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 12 секунд, пока сумма дома не станет равной 100$
    button = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"),"100")
        )
    button1 = browser.find_element_by_css_selector("button.btn")
    button1.click()

    x = browser.find_element_by_xpath("//span[@id='input_value']").text

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(calc(x))

    button2 = browser.find_element_by_css_selector("button[type='Submit']")
    button2.click()

finally:
    time.sleep(5)
    browser.quit()