'''
Возьмите любые 1-3 задачи из прошлых домашних заданий. 
Добавьте к ним логирование ошибок и полезной информации. 
Также реализуйте возможность запуска из командной строки с передачей параметров.
'''

import logging

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
                             f'прямоугольник со сторонами длиной меньше нуля {a = }, {b = }')

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
                             f'прямоугольник со стороной длиной меньше нуля: a = {value}')

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
                             f'прямоугольник со стороной длиной меньше нуля: b = {value}')

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


logging.basicConfig(filename='d:/RepoGB/GB_Python_Specialization/Seminar_15_logging/error.log', level=logging.ERROR, encoding="UTF-8")

if __name__ == '__main__':
    # Блок исключений для создания экземляров класса
    try:
        rect_1 = Rectangle(2, 5)
        print(rect_1.a)
        print(rect_1.b)
        
        rect_1.a = 10
        print(rect_1)
        rect_1.a = 0

        #rect_3 =  Rectangle('2', 5)

    except ValueError or TypeError as e:
        logging.error(f'Возникла ошибка - {e}')
    