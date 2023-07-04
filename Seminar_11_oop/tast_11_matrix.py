"""
    Класс Матрица. 
    Методы для:
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
            триггер = 1 - автозаполнение значениями от 1 до m х n (матрицы размерности m х n, заполненной нулями)
            триггер = 2 - ввод матрицы пользователем (матрицы размерности m х n, заполненной нулями)
            Примечание. Можно доработать через передачу списка (массива)
                        А также передачу другого экземпляра класса
        """
        self.rows = rows            # m - count of rows
        self.columns = columns      # n - count of columns
        match trigger:
            case 0:
                self.user_matrix = [0 for x in range(0, rows * columns)]
            case 1:
                self.user_matrix = [x for x in range(0, rows * columns)]
            case 2:
                self.matrix_input_by_console()

    def matrix_input_by_console(self):
        '''
        Метод для ввода матрицы размерности m х n (частный случай m = n)
        '''
        self.user_matrix = [0 for x in range(0, self.rows * self.columns)]
        for i in range(0, self.rows):
            for j in range(0, self.columns):
                self.user_matrix[i * self.columns + j] = \
                    int(input(f'Введите элемент [{i + 1}][{j + 1}] и нажмите enter: '))

    def matrix_output_to_console (self):
        '''
            Метод для вывода матрицы размерности m х n (частный случай m = n)
        '''
        for i in range(0, self.rows):
            for j in range(0, self.columns):
                print(f'{self.user_matrix[i * self.columns + j]} ', end = '')
            print()

    def matrix_transp(self):
        '''
            Метод для транспонирования матрицы размерности m х n (частный случай m = n)
        '''
        result = [0.0 for x in range(0, self.rows * self.columns)]
        
        for i in range(0, self.rows):
            for j in range(0, self.columns):
                result [j * self.rows + i] = self.user_matrix[i * self.columns + j]
        
        self.user_matrix = result
        if self.rows != self.columns:
            temp = self.rows 
            self.rows = self.columns
            self.columns = self.rows

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

    def __eq__(self, other) -> bool:
        '''
            Переопределенный дандер метод сравнения двух матриц
        '''
        result = True

        if self.rows != other.rows or self.columns != other.columns:
            result = False
        else:
            for i in range(0, self.rows):
                for j in range(0, self.columns):
                    if self.user_matrix[i * self.columns + j] != other.user_matrix[i * other.columns + j]:
                        result = False
                        break
                if not result:
                    break

        return result

    def __multiply__(self, other):
        '''
            Переопределенный дандер метод умножения двух матриц
        '''
        # Две марицы можно умножить тогда и только тогда, когда 
        # количество столбцов первой равно количеству срок второй 
        # Здесь пропускаю обработку исключения на случай невыполнения условия выше

        # создание пустого экземпляра класса
        result = UserMatrix(self.rows, other.columns, 0)
        
        for i in range(0, self.rows):
            for j in range(0, other.columns):
                for k in range(0, self.columns):
                    result.user_matrix[i * other.columns + j] += \
                                                    self.user_matrix[i * self.columns + k] * \
                                                    other.user_matrix[k * other.columns + j]
                    # интерпретация c[i,j] += a[i,k] * b[k,j], 
                    # где i = 1:1:m;   
                    #     j = 1:1:p;  
                    #     k = 1:1:n;  
                    # A[mxn] * B[nxp] = C[mxp]
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
                temp_list_rows_by_int.append(self.user_matrix[i * self.columns + j])
            temp_list_rows_by_str.append(str(temp_list_rows_by_int).strip('[]'))
            temp_list_rows_by_str.append('\n') 
        return " ".join(temp_list_rows_by_str)


if __name__ == '__main__':

    # Создание экземпляров
    matrix_01 = UserMatrix(3, 2, 2)   # вводит пользователь
    matrix_02 = UserMatrix(2, 3, 1)   # вводит пользователь
    matrix_03 = UserMatrix(3, 3, 0)   # нулевая матрица размерности 3 х 3

    # Умножение
    matrix_04 = matrix_01.__multiply__(matrix_02)  # результат матрица 3 * 3
    print()
    print("matrix_01:")
    print(matrix_01.__str__())
    print("matrix_02:")
    print(matrix_02.__str__())
    print("Результат умножения матриц: matrix_01 * matrix_02")
    print(matrix_04.__str__())

    # Сложение
    matrix_05 = matrix_03 + matrix_04       
    # matrix_05 = matrix_03.__add__(matrix_04)
    print("Результат сложения матриц: matrix_03 + matrix_04")
    print(matrix_05.__str__())    
    # Сложение
    matrix_06 = UserMatrix(3, 2, 1)         # вводит пользователь
    matrix_07 = matrix_06 + matrix_01       
    # matrix_07 = matrix_06.__add__(matrix_01)
    print("matrix_06:")
    print(matrix_06.__str__())
    print("matrix_01:")
    print(matrix_01.__str__())
    print("Результат сложения матриц: matrix_06 + matrix_01")
    print(matrix_07.__str__())

    # Другой способ вывода
    print("Результат сложения матриц: matrix_06 + matrix_01")
    matrix_07.matrix_output_to_console()

    # Сравнение
    print()
    print("Результат сравнения матриц: matrix_06 = matrix_01 -> ", end = '')
    print(f"{matrix_06.__eq__(matrix_01)}\n")
    print("Результат сравнения матриц: matrix_06 = matrix_01 -> ", end = '')
    print(f"{matrix_06 == matrix_01}\n")