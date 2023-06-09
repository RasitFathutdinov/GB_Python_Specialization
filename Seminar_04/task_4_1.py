
# 1. Напишите функцию для транспонирования матрицы

def matrix_input (m_rows : int = 2, n_columns : int = 2) -> list:
    result = [0.0 for x in range(0, m_rows * n_columns)]
    for i in range(0, m_rows):
        for j in range(0, n_columns):
            result[i * n_columns + j] = input(f'Введите элемент [{i + 1}][{j + 1}] и нажмите enter: ')
    return result

def matrix_output (m_rows: int, n_columns : int, matrix_to_output : list):
    for i in range(0, m_rows):
        for j in range(0, n_columns):
            print(f'{matrix_to_output[i * n_columns + j]} ', end = '')
        print()

def matrix_transp(m_rows: int, n_columns : int, matrix_gived : list) -> list:
    result = [0.0 for x in range(0, m_rows * n_columns)]
    for i in range(0, m_rows):
        for j in range(0, n_columns):
            result [j * m_rows + i] = matrix_gived[i * n_columns + j]
    return result

# main
rows =  int(input(f'Введите количеств срок матрицы и нажмите enter: '))
columns = int(input(f'Введите количеств столбов матрицы и нажмите enter: '))
my_matrix = matrix_input(rows, columns)

my_matrix_transp = matrix_transp(rows, columns, my_matrix)
rows_transp = columns
columns_transp = rows

print(f'Исходная матрица')
matrix_output(rows, columns, my_matrix)
print(f'Транспорированная матрица')
matrix_output(rows_transp, columns_transp, my_matrix_transp)


#A = [[0] * m for i in range(n)]