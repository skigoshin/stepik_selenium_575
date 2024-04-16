from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# Открыть страницу http://suninjuly.github.io/redirect_accept.html
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)


#Нажать на кнопку
    button1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button1.click()

#Переключиться на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

#Пройти капчу для робота и получить число-ответ

# Посчитать математическую функцию от x
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

# Считать значение для переменной x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)


# Ввести ответ в текстовое поле
    pole1 = browser.find_element(By.ID, "answer")
    pole1.send_keys(y)

# Submit
    button2 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button2.click()





finally:
    time.sleep(10)
    browser.quit()