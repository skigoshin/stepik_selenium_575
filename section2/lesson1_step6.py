from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    # Открыть страницу https://suninjuly.github.io/math.html.
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Найдём этот элемент с помощью WebDriver:
    people_radio = browser.find_element(By.ID, "peopleRule")

    # Найдём атрибут "checked" с помощью встроенного метода get_attribute и проверим его значение:
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

    assert people_checked == "true", "People radio is not selected by default"


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()


