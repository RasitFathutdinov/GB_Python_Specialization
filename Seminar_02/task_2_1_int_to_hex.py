''' Задание
Напишите программу, которая получает целое число и возвращает 
его шестнадцатеричное строковое представление. 

Функцию hex используйте для проверки своего результата.'''

''' Подсказка 1 - Системы счисления
0 hex	=	0 dec	=	0 oct		0	0	0	0	
1 hex	=	1 dec	=	1 oct		0	0	0	1	
2 hex	=	2 dec	=	2 oct		0	0	1	0	
3 hex	=	3 dec	=	3 oct		0	0	1	1	
4 hex	=	4 dec	=	4 oct		0	1	0	0	
5 hex	=	5 dec	=	5 oct		0	1	0	1	
6 hex	=	6 dec	=	6 oct		0	1	1	0	
7 hex	=	7 dec	=	7 oct		0	1	1	1	
8 hex	=	8 dec	=	10 oct		1	0	0	0	
9 hex	=	9 dec	=	11 oct		1	0	0	1	
A hex	=	10 dec	=	12 oct		1	0	1	0	
B hex	=	11 dec	=	13 oct		1	0	1	1	
C hex	=	12 dec	=	14 oct		1	1	0	0	
D hex	=	13 dec	=	15 oct		1	1	0	1	
E hex	=	14 dec	=	16 oct		1	1	1	0	
F hex	=	15 dec	=	17 oct		1	1	1	1
'''

''' Подсказка 2 - Перевод
0101 1010 0011  (base 2) = 5A3 (base 16) = {5*16**2 + 10*16**1 + 3*16**0} = 1443 (base 10) 

'''

# Константа
NUMBER_BASE_10 = 1443 

# Переменные
temp_number_base_10 = NUMBER_BASE_10        # число для деления в цикле
number_base_02 = ''                         # строка для сбора в 2 с/с

# перевод в 2 с/с
while temp_number_base_10 > 0:
    number_base_02 = str(temp_number_base_10 % 2) +  number_base_02
    temp_number_base_10 = temp_number_base_10 // 2
    #print(f'{NUMBER_BASE_10} -> {number_base_02}')

# дозаполение нулей в полученном числе
len_number_base_02 = len(number_base_02)
while(len_number_base_02 % 4 != 0):
    number_base_02 = '0' + number_base_02   # добавляем слева ноль
    len_number_base_02 += 1                 #  увеличиваем длину на 1
    #print(f'{number_base_02} - {len_number_base_02} - {len_number_base_02 % 4}')

# преобразование 2 с/с в 16 с/с
count_of_repeat = len_number_base_02 / 4
pos_begin = 0
pos_end = 4
number_base_16 = ''
while count_of_repeat > 0:
    # разбиение на четвёрки
    temp_str = number_base_02[pos_begin:pos_end]
    #print(f'{count_of_repeat} - {pos_end} - {pos_begin} - {temp_str}')
    count_of_repeat -= 1
    pos_end += 4
    pos_begin += 4
    # преобразование четвёрок в 16 с/с
    match temp_str:
        case '0000':                                  # 0
            number_base_16 = number_base_16 + '0'                    
        case '0001':                                  # 1
            number_base_16 = number_base_16 + '1'
        case '0010':                                  # 2
            number_base_16 = number_base_16 + '2'
        case '0011':                                  # 3
            number_base_16 = number_base_16 + '3'
        case '0100':                                  # 4
            number_base_16 = number_base_16 + '4'
        case '0101':                                  # 5
            number_base_16 = number_base_16 + '5'
        case '0110':                                  # 6
            number_base_16 = number_base_16 + '6'
        case '0111':                                  # 7
            number_base_16 = number_base_16 + '7'
        case '1000':                                  # 8
            number_base_16 = number_base_16 + '8'
        case '1001':                                  # 9
            number_base_16 = number_base_16 + '9'
        case '1010':                                  # A (10)
            number_base_16 = number_base_16 + 'A'
        case '1011':                                  # B (11)
            number_base_16 = number_base_16 + 'B'
        case '1100':                                  # C (12)
            number_base_16 = number_base_16 + 'C'
        case '1101':                                  # D (13)
            number_base_16 = number_base_16 + 'D'
        case '1110':                                  # E (14)
            number_base_16 = number_base_16 + 'E'
        case '1111':                                  # F (15)
            number_base_16 = number_base_16 + 'F'

print(f'{NUMBER_BASE_10} -> {number_base_02} -> {number_base_16}')