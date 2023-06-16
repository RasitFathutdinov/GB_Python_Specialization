# Урок 6. Модули

# Задача 2. Добавьте в пакет, созданный на семинаре шахматный модуль. 
# Внутри него напишите код, решающий задачу о 8 ферзях. 
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. 
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. 
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

# если дадите ещё время - к вечеру субботы выполню


'''
Идея и порядок решения/выполнения

Задача двухмерного динаического программирования.

Использую двухмерные списки.
    двухмерный список размерностью m x n буду лениаризовать как на С++ через одномерный список m * n
        a[i,j] = a[i*n + j]

Идея понятна, формирую игровое поле, где есть граница, за которую ходить нельзя.
    После постановки ферзя на поле, едёр расчёт его зоны охвата 
    (вертикальный крест, боковой/диагональный крест) до границ
        там где уже стоит ферзь - будут 1, 2, 3, 4, 5, 6, 7, 8, 9
        там где поле битое (ф зоне охвата другого ферзя) -1 (т.е. ячейка занята)
            Можно попробовать схитрить, используя список из строк
                собирать отдельно в строку на каждую ячейку, которую охватывает каждый ферзь
                    например 12  или 489 - это значит ячей в "зоне охвата" ферзя 1 и 3 или 4 и 8 и 9
  0 1 2 3 4 5 6 7 8 9 
0 0 0 0 0 0 0 0 0 0 0
1 0 - - - - - - - - 0
2 0 - - - - - - - - 0
3 0 - - - - - - - - 0
4 0 - - - - - - - - 0
5 0 - - - - - - - - 0
6 0 - - - - - - - - 0
7 0 - - - - - - - - 0
8 0 - - - - - - - - 0
9 0 0 0 0 0 0 0 0 0 0

Готовлю матрицу смежности, где вместо ? для бьющих друг друга 1, не бьющих 0 
    1 2 3 4 5 6 7 8 
1   - ? ? ? ? ? ? ?
2   ? - ? ? ? ? ? ?
3   ? ? - ? ? ? ? ?
4   ? ? ? - ? ? ? ?
5   ? ? ? ? - ? ? ?
6   ? ? ? ? ? - ? ?
7   ? ? ? ? ? ? - ?
8   ? ? ? ? ? ? ? -

'''