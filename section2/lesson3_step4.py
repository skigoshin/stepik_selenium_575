from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    # Открыть страницу http://suninjuly.github.io/alert_accept.html
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Посчитать математическую функцию от x (код для этого приведён ниже).
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    # Нажать на кнопку I want to go on a magical journey!.
    button1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button1.click()
    
    # модальное окно confirm, говорим Да
    confirm = browser.switch_to.alert
    confirm.accept()

    # Считать значение для переменной x.
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    # Ввести ответ в текстовое поле.
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    
    # Нажать на кнопку Submit.
    button2 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button2.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


