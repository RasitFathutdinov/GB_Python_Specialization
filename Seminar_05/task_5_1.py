# Урок 5. Интераторы и генераторы

# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os

def get_file_path_parts(file_full_path : str = 'C:\file.txt') -> tuple:
    temp = os.path.basename(file_full_path)
    index = temp.index('.')
    file_name = temp[:index]
    file_extension = temp[index:]
    #file_extension = os.path.splitext(file_full_path)[1]
    file_path = file_full_path.replace(temp, '')
    result = (file_path, file_name, file_extension)
    # print(f'file_path = {file_path}')
    # print(f'file_name = {file_name}')
    # print(f'file_extension = {file_extension}')
    return result 

if not os.path.exists('D:\RepoGB\GB_Python_Specialization\empty_file_for_1st_task.txt'):
    path_absolute = 'D:\RepoGB\GB_Python_Specialization\empty_file_for_1st_task.txt'   
else:
    path_absolute = os.path.abspath('empty_file_for_1st_task.txt')
print(path_absolute)

print(get_file_path_parts(path_absolute))

