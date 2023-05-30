# Семинар № 1 Задание № 3
'''
Программа загадывает число от 0 до 1000. 

Необходимо угадать число за 10 попыток. 
Программа должна подсказывать “больше” или “меньше” после каждой попытки. 

Для генерации случайного числа используйте код:
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)
'''

from random import randint

# Константы
LOWER_LIMIT = 0                 
UPPER_LIMIT = 1000

# Переменные
numer_random = randint(LOWER_LIMIT, UPPER_LIMIT)
flag_trying_to_guess = True
trying_to_guess = 10

while flag_trying_to_guess:
    number_user = int(input(f"\nВведите целое число от {LOWER_LIMIT} до {UPPER_LIMIT} и нажмите Enter: "))
    trying_to_guess -= 1
    if number_user <= LOWER_LIMIT or number_user >= UPPER_LIMIT:
        print(f"Несоответствующее значение диапазону {LOWER_LIMIT} до {UPPER_LIMIT} . \n Минус одна попытка!")
    elif number_user == numer_random:
        print(f"Вы угадали число! Загадано: {numer_random}, введено: {number_user}")
    elif number_user > numer_random:
         print(f"Загадано меньше, введеного: {number_user}\n Осталось попыток {trying_to_guess}!")
    else:
         print(f"Загадано больше, введеного: {number_user}\n Осталось попыток {trying_to_guess}!")
    if trying_to_guess == 0:
        flag_trying_to_guess = False    

if flag_trying_to_guess:
    print("\nВы молодец!")
else:
    print(f"\nЗагадано было {numer_random}")
    print("Может быть Вам повезёт в следующий раз.\n") 