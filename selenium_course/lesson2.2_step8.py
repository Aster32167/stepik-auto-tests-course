from selenium import webdriver
import time
import os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    input1 = browser.find_element_by_css_selector("input[placeholder='Enter first name']")
    input1.send_keys('First name')
    input2 = browser.find_element_by_css_selector("input[placeholder='Enter last name']")
    input2.send_keys('Last name')
    input3 = browser.find_element_by_css_selector("input[placeholder='Enter email']")
    input3.send_keys('mail@mail.ru')

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла

    element = browser.find_element_by_id("file")
    element.send_keys(file_path)

    button = browser.find_element_by_tag_name("button")
    button.click()
finally:
    time.sleep(5)
    browser.quit()