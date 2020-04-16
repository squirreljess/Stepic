from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
roomPrice = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

button = browser.find_element_by_id("book")
button.click()

x_element = browser.find_element_by_css_selector("#input_value")
x = x_element.text


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


y = calc(x)
y_element = browser.find_element_by_css_selector("#answer")
y_element.send_keys(y)

submit = browser.find_element_by_id("solve")
submit.click()

