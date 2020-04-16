# lesson1 selectors

from selenium import webdriver
import math
from selenium.webdriver.support.ui import Select

# lesson2 selectors + click

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/xpath_examples")
goldButton = driver.find_element_by_xpath("//button[text()='Gold']")
goldButton.click()

driver.quit()

# LESSON3

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/math.html")

x_element = driver.find_element_by_css_selector("#input_value")
x = x_element.text


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


y = calc(x)
y_element = driver.find_element_by_css_selector("#answer")
y_element.send_keys(y)

checkBox = driver.find_element_by_css_selector("#robotCheckbox")
checkBox.click()

radio = driver.find_element_by_css_selector("#robotsRule")
radio.click()

submit = driver.find_element_by_css_selector(".btn.btn-default")
submit.click()

driver.quit()

# LESSON4

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/get_attribute.html")

x_element = driver.find_element_by_css_selector("#treasure")
x = x_element.get_attribute("valuex")


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


y = calc(x)
y_element = driver.find_element_by_css_selector("#answer")
y_element.send_keys(y)

checkBox = driver.find_element_by_css_selector("#robotCheckbox")
checkBox.click()

radio = driver.find_element_by_css_selector("#robotsRule")
radio.click()

submit = driver.find_element_by_css_selector(".btn.btn-default")
submit.click()

driver.quit()

# lesson5

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/selects1.html")

x = driver.find_element_by_css_selector("#num1").text
y = driver.find_element_by_css_selector("#num2").text

z = str(str(int(x) + int(y)))

# driver.find_element_by_tag_name("select").click()
# browser = driver.find_element_by_css_selector("[value='z']")
# browser.click()

select = Select(driver.find_element_by_tag_name("select"))
select.select_by_value(z)

submit = driver.find_element_by_css_selector(".btn.btn-default")
submit.click()

driver.quit()

# lesson6

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/execute_script.html")

x_element = driver.find_element_by_css_selector("#input_value")
x = x_element.text


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


y = calc(x)
y_element = driver.find_element_by_css_selector("#answer")
y_element.send_keys(y)

checkBox = driver.find_element_by_css_selector("#robotCheckbox")
checkBox.click()

driver.execute_script("window.scrollBy(0, 120);")

radio = driver.find_element_by_css_selector("#robotsRule")
radio.click()

submit = driver.find_element_by_css_selector(".btn.btn-primary")
submit.click()

driver.quit()
