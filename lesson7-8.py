from selenium import webdriver
import math

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/redirect_accept.html")

submit = driver.find_element_by_css_selector(".trollface.btn.btn-primary")
submit.click()

new_window = driver.window_handles[1]
driver.switch_to.window(new_window)

# confirm = driver.switch_to.alert
# confirm.accept()

x_element = driver.find_element_by_css_selector("#input_value")
x = x_element.text


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


y = calc(x)
y_element = driver.find_element_by_css_selector("#answer")
y_element.send_keys(y)

submit = driver.find_element_by_css_selector(".btn.btn-primary")
submit.click()
