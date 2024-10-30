from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    # Открыть страницу http://suninjuly.github.io/get_attribute.html.
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Посчитать математическую функцию от x (код для этого приведён ниже).
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    # Считать значение для переменной x.
    x_element = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    # Ввести ответ в текстовое поле.
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    
    # Отметить checkbox "I'm the robot".
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()

    # Выбрать radiobutton "Robots rule!".
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()

    # Нажать на кнопку Submit.
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()


