#если файлы lesson2_step7.py и file.txt" лежат в одном каталоге

# импортируем модуль
import os

# получаем путь к директории текущего исполняемого скрипта lesson2_step7.py
current_dir = os.path.abspath(os.path.dirname(__file__))

# имя файла, который будем загружать на сайт
file_name = "file.txt"

# получаем путь к file.txt
file_path = os.path.join(current_dir, file_name)

# отправляем файл
element.send_keys(file_path)