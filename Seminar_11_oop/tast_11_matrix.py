"""
    Класс Матрица. 
    Добавьте методы для:
        вывода на печать,
        сравнения,
        сложения,
        *умножения матриц
"""


class UserMatrix:
    def __init__(self, rows: int = 2, columns: int = 2, trigger : int = 1):
        """
        Конструктор - инициализация экземпляра класса
            триггер = 0 - создание нулевой марицы (матрицы размерности m х n, заполненной нулями)
            триггер = 1 - ввод матрицы пользователем (матрицы размерности m х n, заполненной нулями)
            Примечание. Можно доработать через передачу списка (массива)
                        А также передачу другого экземпляра класса
        """
        self.rows = rows            # m - count of rows
        self.columns = columns      # n - count of columns
        self.user_matrix = [0 for x in range(0, rows * columns)]
        self.user_matrix = self.matrix_input_by_console(rows, columns)

    def matrix_input_by_console (m_rows : int = 2, n_columns : int = 2) -> list:
        '''
        Метод для ввода матрицы размерности m х n (частный случай m = n)
        '''
        result = [0.0 for x in range(0, * n_columns)]
        for i in range(0, m_rows):
            for j in range(0, n_columns):
                result[i * n_columns + j] = input(f'Введите элемент [{i + 1}][{j + 1}] и нажмите enter: ')
        return result

    def matrix_output_to_console (m_rows: int, n_columns : int, matrix_to_output : list):
        '''
            Метод для вывода матрицы размерности m х n (частный случай m = n)
        '''
        for i in range(0, m_rows):
            for j in range(0, n_columns):
                print(f'{matrix_to_output[i * n_columns + j]} ', end = '')
            print()

    def matrix_transp(m_rows: int, n_columns : int, matrix_gived : list) -> list:
        '''
            Метод для транспонирования матрицы размерности m х n (частный случай m = n)
        '''
        result = [0.0 for x in range(0, m_rows * n_columns)]
        for i in range(0, m_rows):
            for j in range(0, n_columns):
                result [j * m_rows + i] = matrix_gived[i * n_columns + j]
        return result

    def __add__(self, other):
        '''
            Переопределенный дандер метод сложения двух матриц
        '''
        # Две марицы можно сложить тогда и только тогда, когда их размерности равны
        # Здесь пропускаю обработку исключения на случай несовпадения размерности матриц

        # создание пустого экземпляра класса
        result = UserMatrix(self.rows, self.columns, 0)

        # сложение поэлементное
        for i in range(0, self.rows):
            for j in range(0, self.columns):
                result.user_matrix[i * result.columns + j] = \
                    self.user_matrix[i * self.columns + j] + \
                    other.user_matrix[i * other.columns + j]
                
        return result

    def __multiply__(self, other):
        '''
            Переопределенный дандер метод умножения двух матриц
        '''
        # Две марицы можно умножить тогда и только тогда, когда 
        # количество столбцов первой равно количеству срок второй 
        # Здесь пропускаю обработку исключения на случай невыполнения условия выше

        # создание пустого экземпляра класса
        result = UserMatrix(self.rows, self.columns, 0)

        # for i in range(0, self.rows):
        #     for j in range(0, self.columns):
        #         result.user_matrix[i * result.columns + j] = \
        #             self.user_matrix[i * self.columns + j] + \
        #             other.user_matrix[i * other.columns + j]
        
        return result        

    def __str__(self):
        '''
            Переопределенный дандер метод в преобразования в строку экземпляра класса
            для дальнейшего вывода (консоль, текстовое поле или файл)
        '''
        temp_list_rows_by_str = []
        for i in range(0, self.rows):
            temp_list_rows_by_int = []
            for j in range(0, self.columns):
                # print(f'{matrix_to_output[i * n_columns + j]} ', end = '')
                temp_list_rows_by_int.append(self.user_matrix[i * self.columns + j])
            temp_list_rows_by_str.append(str(temp_list_rows_by_int).strip('[]'))
            temp_list_rows_by_str.append('\n') 
        return " ".join(temp_list_rows_by_str)


if __name__ == '__main__':

    # Создание экземпляров
    matrix_01 = UserMatrix(3, 2, 1)   # вводит пользователь
    matrix_02 = UserMatrix(2, 3, 1)   # вводит пользователь
    matrix_03 = UserMatrix(3, 3, 0)   # нулевая матрица размерности 3 х 3

    # Умножение
    matrix_04 = matrix_01.__multiply__(matrix_02)  # результат матрица 3 * 3
    matrix_04.__str__()
    # Сложение
    matrix_05 = matrix_03 + matrix_04               # результат матрица 3 * 3
    matrix_05.__str__()


