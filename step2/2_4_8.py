from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)


# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element из библиотеки expected_conditions.

    wait = WebDriverWait(browser, 12)
    element = wait.until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    
# Нажать на кнопку "Book"
    button = browser.find_element(By.ID, "book")
    button.click()

# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
# Посчитать математическую функцию от x
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
# Считать значение для переменной x    
    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = x_element.text
    y = calc(x)

# Ввести ответ в текстовое поле
    pole1 = browser.find_element(By.ID, "answer")
    pole1.send_keys(y)


# Нажать на кнопку "Submit"
    button = browser.find_element(By.ID, "solve")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


