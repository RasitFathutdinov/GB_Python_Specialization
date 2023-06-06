
# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов. 
# За основу возьмите любую статью из википедии или из документации к языку.

import re

base_text = "Решить задачи, которые не успели решить на семинаре. \
                    Дан список повторяющихся элементов \
                    Дан список повторяющихся элементов \
                    Дан список повторяющихся элементов \
                    Дан список повторяющихся элементов \
                    Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. \
                    В результирующем списке не должно быть дубликатов."
                   
#  В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. \
#                     В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. \
#                     Не учитывать знаки препинания и регистр символов. \
#                     За основу возьмите любую статью из википедии или из документации к языку. \
#                     Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. \
#                     Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. \
#                     Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака."

СOUNT_WORDS_TO_OUTPUT = 10      # количество самых частых встречаемых слов = 10 

# список из слов текста
list_of_full_words = ((base_text.lower()).strip(".,!?;^-+*/<>=_0123456789")).split()     

# список из неповторяющихся слов текста
list_words_without_repeat = [*set(list_of_full_words)]

# список для хранения количества повторов (вместо словаря)
list_count_word_repeat = [0 for x in range(0, len(list_words_without_repeat))]
# ищем количество вхождений и сохраняем во второй список
for i, item_searched in enumerate(list_words_without_repeat):
    count_of_entry = 0
    for j, item in enumerate(list_of_full_words):
        if item == item_searched:
            count_of_entry +=1
    list_count_word_repeat[i] = count_of_entry

# формирование вложенного списка вместо словаря
my_list = []
for j in range (0, len(list_words_without_repeat)):
    my_list.append([list_count_word_repeat[j], list_words_without_repeat[j]])

print(f"Список из исходного текста:\n {list_of_full_words}\n")
print(f"Список количества повторов и слов:\n {my_list}\n")

# Сортировка для вывода первых 10-ти (вернуть 10 самых частых)
my_list.sort(reverse=True)
print(f"Отсортированный список количества повторов и слов:\n {my_list}\n")

# вернуть 10 самых частых слов
if len(my_list) < СOUNT_WORDS_TO_OUTPUT:
    print(f"Отсортированный список количества повторов и слов:\n {my_list}\n")
else:
    print(f"10 самых частых слов:\n {my_list[0:СOUNT_WORDS_TO_OUTPUT]}\n")


############################## Через словари ############################## 
my_dict = {list_words_without_repeat[i]: list_count_word_repeat[i] for i in range(0, len(list_words_without_repeat), 1)} 
#print(my_dict)
# Для сортировать словарь по значению укажем в качестве ключа сортировки индекс значения словаря в полученном списке кортежей: 
# lambda x: x[1], где x - это кортеж (key, val)
sorted_tuple = sorted(my_dict.items(), reverse=True, key=lambda x: x[1] )
# преобразовываем обратно в словарь
my_dict = dict(sorted_tuple)
#print("\n")
#print(my_dict)
# вернуть 10 самых частых слов
print("10 самых частых слов (через словарь):\n")
count = 0
if len(my_dict) < СOUNT_WORDS_TO_OUTPUT:
    for key,value in my_dict.items():
        count += 1 
        print('#', count, ' - ',  key, ':', value)
else:
    for key,value in my_dict.items(): 
        count += 1
        if count > СOUNT_WORDS_TO_OUTPUT:
            break
        print('#', count, ' - ',  key, ':', value)
        
