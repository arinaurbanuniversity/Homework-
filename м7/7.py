import os
import time

directory = "C:\\Users\\Admin\\PycharmProjects\\Urban"

try:
       for root, dirs, files in os.walk(directory):
           for file in files:
               filepath = os.path.join(root, file)

               filetime = os.path.getmtime(filepath)
               formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

               filesize = os.path.getsize(filepath)

               parent_dir = os.path.dirname(filepath)

               print(
                   f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: '
                   f'{formatted_time}, Родительская директория: {parent_dir}')
except Exception as e:
       print(f"Произошла ошибка: {e}")