from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:

    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("firstname")
    
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("lastname")
 

    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("email")
 
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']") # находим место добавления файла
    element.send_keys(file_path) #добавляем файл

    # Нажать на кнопку Submit.
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()


