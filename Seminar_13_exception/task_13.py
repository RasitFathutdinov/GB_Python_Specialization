# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях. 
# Напишите к ним классы исключения с выводом подробной информации. 
# Поднимайте исключения внутри основного кода. 
# Например нельзя создавать прямоугольник со сторонами отрицательной длины.

# Решение
class Rectangle:
    '''Класс прямоугольник, с методами расчета периметра и площади фигуры.'''

    def __init__(self, a: int, b: int = None):
        '''Метод инициализации прямоугольника со сторонами a и b.'''
        # Проверка на значение
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError(f'Длина стороны прямоугольника должна быть числом. Используйте int или float. {type(a)}, {type(b)}')
        # Проверка на тип даных
        if a > 0 and b > 0:
            self._a = a
            self._b = b if b is not None else a
        else:
            raise ValueError('В поле действительных чисел нельзя создавать' +
                             f'прямоугольник со сторонами отрицательной длины {a = }, {b = }')

    #Свойства
    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @a.setter
    def a(self, value):        
        if not isinstance(value, (int, float)):
            raise TypeError('Длина стороны прямоугольника должна быть числом.' + 
                            f' Используйте int или float. {type(value) = }')
        # Проверка на тип даных
        if value > 0:
            self._a = value
        else:
            raise ValueError('В поле действительных чисел нельзя создавать' +
                             f'прямоугольник со стороной отрицательной длины a = {value}')

    @b.setter
    def b(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Длина стороны прямоугольника должна быть числом.' + 
                            f' Используйте int или float. {type(value) = }')
        # Проверка на тип даных
        if value > 0:
            self._b = value
        else:
            raise ValueError('В поле действительных чисел нельзя создавать' +
                             f'прямоугольник со стороной отрицательной длины b = {value}')

    # Методы
    def perimeter(self):
        '''Метод расчета периметра прямоугольника.'''
        return 2 * (self.a + self.b)

    def area(self):
        '''Метод расчета площади прямоугольника.'''
        return self.a * self.b

    def __str__(self):
        '''Переопределенный дандер метод строчного выведения экземпляра класса'''
        return f'Прямоугольник {self.a} x {self.b}'

    # Переопределение математическихопераций
    def __add__(self, other):
        '''Переопределенный дандер метод сложения двух прямоугольников.'''
        new_perimeter = self.perimeter() + other.perimeter()
        new_a = self.a
        new_b = new_perimeter / 2 - new_a
        return Rectangle(new_a, new_b)

    def __sub__(self, other):
        '''Переопределенный дандер метод вычетания двух прямоугольников.'''
        new_perimeter = abs(self.perimeter() - other.perimeter())
        new_a = min([self.a, self.b, other.a, other.b])
        new_b = new_perimeter / 2 - new_a
        return Rectangle(new_a, new_b)



if __name__ == '__main__':
    # Блок исключений для создания экземляров класса
    try:
        rect_1 = Rectangle(2, 5)
        print(rect_1.a)
        print(rect_1.b)
        
        rect_1.a = 10
        print(rect_1)
        rect_1.a = 0

    except ValueError or TypeError as e:
        print(f'Инициализация или переопределение экземпляра класса привело к ошибке ValueError: {e}')
    

    #Блок слежующих исключений для другой части кода относительно решаемой задачи
    # - мат опреации
    # - или непосредсвеннаря работа в другом коде или с другими класса где есть ошибки ввода и вывода
    
