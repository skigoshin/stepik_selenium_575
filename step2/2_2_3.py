from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

# Подсчет данных
    def calc(x, y):
        return str(int(x) + int(y))

# Посчитать сумму заданных чисел
# Найти первое число
    num1 = browser.find_element(By.ID, "num1")
    x = num1.text
# Найти второе число
    num2 = browser.find_element(By.ID, "num2")
    y = num2.text
# Сумма
    sum = calc(x, y)


# Выбрать в выпадающем списке значение равное расчитанной сумме
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum)

# Нажать на кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

