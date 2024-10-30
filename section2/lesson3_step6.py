from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    # Открыть страницу http://suninjuly.github.io/redirect_accept.html
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Посчитать математическую функцию от x (код для этого приведён ниже).
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    # Нажать на кнопку I want to go on a magical journey!.
    button1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button1.click()

    # запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться
    # first_window = browser.window_handles[0]

    # Чтобы узнать имя новой вкладки, нужно использовать метод window_handles, который возвращает массив имён всех вкладок.
    # Зная, что в браузере теперь открыто две вкладки, выбираем вторую вкладку:
    new_window = browser.window_handles[1]
    
    # Для переключения на новую вкладку надо явно указать, на какую вкладку мы хотим перейти
    browser.switch_to.window(new_window)

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


