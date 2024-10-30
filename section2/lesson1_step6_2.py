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

    print(people_radio.get_attribute("name"))
    # Напечатает ruler, т.е. текстовое значение аттрибута

    print(people_radio.get_attribute("checked"))
    # Напечатает true, т.е. факт того что аттрибут существует. Учтите что true это в данном случае строка, а не булево значение.

    print(people_radio.get_attribute("href"))
    # Напечатает None, т.к. аттрибут не существует. И это не строка а None-значение.

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()


