from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Открыть страницу http://suninjuly.github.io/file_input.html
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

# Заполнить текстовые поля: имя, фамилия, email
    pole_first = browser.find_element(By.CSS_SELECTOR, "div.form-group input[name='firstname']")
    pole_first.send_keys('test_first')

    pole_last = browser.find_element(By.CSS_SELECTOR, "div.form-group input[name='lastname']")
    pole_last.send_keys('test_last')

    pole_email = browser.find_element(By.CSS_SELECTOR, "div.form-group input[name='email']")
    pole_email.send_keys('test_email')




# Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    button_file = browser.find_element(By.ID, "file")    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, '2_2_8.txt')           # добавляем к этому пути имя файла 
    button_file.send_keys(file_path)


# Нажать кнопку "Submit"
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()