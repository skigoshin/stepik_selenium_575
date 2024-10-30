from selenium import webdriver
import time
try:
    browser = webdriver.Chrome()
    browser.execute_script("alert('Robots at work');")
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

