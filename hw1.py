from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math as m
import pyperclip


def y(z):
    return m.log(abs(12 * m.sin(z)))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

WebDriverWait(browser, 10000).until(
    EC.text_to_be_present_in_element((By.ID, 'price'), '100')
)
browser.find_element_by_class_name('btn').click()
x = int(browser.find_element_by_id('input_value').text)
browser.find_element_by_css_selector('input').send_keys(str(y(x)))
browser.find_element_by_id('solve').click()
pyperclip.copy(browser.switch_to.alert.text.split(' ')[-1])
browser.switch_to.alert.accept()
browser.quit()
