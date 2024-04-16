from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)




# Посчитать математическую функцию от x
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

# Считать значение для переменной x 
# Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
    sunduk = browser.find_element(By.ID, "treasure")
# Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
    x = sunduk.get_attribute("valuex")
    y = calc(x)

# Ввести ответ в текстовое поле
    pole1 = browser.find_element(By.ID, "answer")
    pole1.send_keys(y)
# Отметить checkbox "I'm the robot"
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
# Выбрать radiobutton "Robots rule!"
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()
# Нажать на кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

