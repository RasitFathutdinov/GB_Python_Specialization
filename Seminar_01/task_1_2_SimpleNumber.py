# Семинар № 1 Задание № 2
'''
Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 

Используйте правило для проверки: 
“Число является простым, если делится нацело только на единицу и на себя”. 

Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
'''
def num_is_simple(input_number)->bool:
    '''
    Функция для проверки на простое число.
        Простое число — натуральное число, имеющее ровно два различных натуральных делителя. 
        Другими словами, натуральное число "p" является простым, если оно отлично от 1 
        и делится без остатка только на 1 и на само p
    '''
    if input_number == 1:       # первое простое => сразу возврат истина
        result = True
    elif input_number > 2:
        result = True
        for divider in range(2, input_number):
            if input_number % divider == 0:
                result = False  # при первом же делении нацело возвращаем не простое
                break
    else:
        result = False          # 1 и отрицательные не простые
    return result


try:
    number = int(input("\nВведите натуральное число от 1 до 100 000: "))
    if number <= 0 or number >= 100000:
        raise ValueError("Несоответствующее значение")
except ValueError as error:
    print(f"Некорректный ввод, введено число вне диапазона от 1 до 100 000")
except:
    print("Ошибка при преобразовании в число целого типа")
else:
    answere = num_is_simple(number)
    print(f"{number} - число простое : {answere}")
finally:
    print("Завершено выполнение программы...\n")