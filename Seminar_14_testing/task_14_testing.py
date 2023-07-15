'''
    Тестирование черз doctest методов для
        - транспорирования матрицы
        - преобразования матрицы в строку
'''

import doctest
import string

# # 1. Напишите функцию для транспонирования матрицы
# def matrix_input (m_rows : int = 2, n_columns : int = 2) -> list:
#     result = [0.0 for x in range(0, m_rows * n_columns)]
#     for i in range(0, m_rows):
#         for j in range(0, n_columns):
#             result[i * n_columns + j] = input(f'Введите элемент [{i + 1}][{j + 1}] и нажмите enter: ')
#     return result

# def matrix_output (m_rows: int, n_columns : int, matrix_to_output : list):
#     for i in range(0, m_rows):
#         for j in range(0, n_columns):
#             print(f'{matrix_to_output[i * n_columns + j]} ', end = '')
#         print()

def matrix_transp(m_rows: int, n_columns : int, matrix_gived : list) -> list:
    '''
    text
    >>> matrix_transp(2, 3, [1, 2, 3, 4, 5, 6])
    [1, 4, 2, 5, 3, 6]
    >>> matrix_transp(2, 3, [6, 5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5, 6]
    '''
    result = [0.0 for x in range(0, m_rows * n_columns)]
    for i in range(0, m_rows):
        for j in range(0, n_columns):
            result [j * m_rows + i] = matrix_gived[i * n_columns + j]
    return result

# def matrix_to_string (m_rows: int, n_columns : int, matrix_to_str : list) -> string:
#     '''
#     text
#     >>> matrix_to_string(2, 3, [1, 2, 3, 4, 5, 6])
#     '[\\n1, 2, 3\\n4, 5, 6\\n]'
#     >>> matrix_to_string(2, 3, [1, 2, 3, 4, 5, 6])
#     1, 2, 3, 4, 5, 6
#     '''
#     list_of_rows = ['[']
#     for i in range(0, m_rows):
#         list_of_rows.append(str(matrix_to_str[i * n_columns : (i+1) * n_columns]).strip('[]'))

#     list_of_rows.append(']')
#     result = '\n'.join(list_of_rows)
#     return result


if __name__ == '__main__':
    doctest.testmod(verbose=True)

    # # тест "1" - успешный 
    # my_matrix = [1, 2, 3, 4, 5, 6]
    # my_matrix_transp = matrix_transp(2, 3, my_matrix)
    # print(f'Исходная матрица')
    # print(f'{my_matrix}')
    # matrix_output(2, 3, my_matrix)
    # print(f'Транспорированная матрица')
    # print(f'{my_matrix_transp}')
    # matrix_output(3, 2, my_matrix_transp)

    # # тест "2" - провал 
    # my_matrix_02 = [6, 5, 4, 3, 2, 1]
    # my_matrix_transp_02 = matrix_transp(3, 2, my_matrix_02)
    # print(f'Исходная матрица')
    # matrix_output(3, 3, my_matrix_02)
    # print(f'Транспорированная матрица')
    # matrix_output(f'{my_matrix_transp_02}')

    # # тест "1*" - успешный 
    # print(matrix_to_string(2, 3, [1, 2, 3, 4, 5, 6]))

    # # тест "2*" - провал 
    # print(matrix_to_string(2, 3, [6, 5, 4, 3, 2, 1]))
    
    #################  тестирование !matrix_to_string!    ############

#   print(matrix_to_string(2, 3, [1, 2, 3, 4, 5, 6]))

#     PS D:\RepoGB\GB_Python_Specialization> ... task_14_testing.py
#     Trying:
#         matrix_to_string(2, 3, [1, 2, 3, 4, 5, 6])
#     Expecting:
#         '[\n1, 2, 3\n4, 5, 6\n]'
#     ok
#     Trying:
#         matrix_to_string(2, 3, [1, 2, 3, 4, 5, 6])
#     Expecting:
#         1, 2, 3, 4, 5, 6
#     **********************************************************************
#     File "d:\RepoGB\GB_Python_Specialization\Seminar_14_testing\task_14_testing.py", line 37, in __main__.matrix_to_string
#     Failed example:
#         matrix_to_string(2, 3, [1, 2, 3, 4, 5, 6])
#     Expected:
#         1, 2, 3, 4, 5, 6
#     Got:
#         '[\n1, 2, 3\n4, 5, 6\n]'
#     1 items had no tests:
#         __main__
#     **********************************************************************
#     1 items had failures:
#     1 of   2 in __main__.matrix_to_string
#     2 tests in 2 items.    
#     1 passed and 1 failed.


  #################  тестирование !matrix_transp!    ############
#     PS D:\RepoGB\GB_Python_Specialization> ... task_14_testing.py
    # Trying:
    #     matrix_transp(2, 3, [1, 2, 3, 4, 5, 6])
    # Expecting:
    #     [1, 4, 2, 5, 3, 6]
    # ok
    # Trying:
    #     matrix_transp(2, 3, [6, 5, 4, 3, 2, 1])
    # Expecting:
    #     [1, 2, 3, 4, 5, 6]
    # **********************************************************************

    # Failed example:
    #     matrix_transp(2, 3, [6, 5, 4, 3, 2, 1])
    # Expected:
    #     [1, 2, 3, 4, 5, 6]
    # Got:
    #     [6, 3, 5, 2, 4, 1]
    # 3 items had no tests:
    #     __main__
    #     __main__.matrix_input
    #     __main__.matrix_output
    # **********************************************************************
    # 1 items had failures:
    #     1 of   2 in __main__.matrix_transp
    # 2 tests in 4 items.
    # 1 passed and 1 failed.
    # ***Test Failed*** 1 failures.
    # PS D:\RepoGB\GB_Python_Specialization>