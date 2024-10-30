from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x1_element = browser.find_element(By.ID, "num1")
    x1 = x1_element.text

    x2_element = browser.find_element(By.ID, "num2")
    x2 = x2_element.text

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(int(x1) + int(x2)))

    # Нажать на кнопку Submit.
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()


