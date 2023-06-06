'''
Дан список повторяющихся элементов. 

Вернуть список с дублирующимися элементами. 
В результирующем списке не должно быть дубликатов.
'''

#В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.
#Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака


# 2 - Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов 
# исходной последовательности. 
# Не использовать множества.
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]


def input_list_of_nums(output_string):
    '''
    Данный метод рекурсивно предлгагает пользователю корректно ввести список
    Рекурсия, чтоб не использовать цикл
    '''
    result = []
    bool_need_reinput = True
    try:
        result = list(map(int, input(output_string).split()))        
        assert len(result) > 1, "Вы не ввели список, нужно ввести не менее 1 числа!" # от обратного
        bool_need_reinput = False 
    except AssertionError as err:   
        print(err)                             
    except:                                                               
        print("Ошибка при вводе списка из чисел!")
    else:
        # print("\tУспешно введён список из чисел.")
        print('')
    finally:
        if bool_need_reinput:
            result = input_list_of_nums(output_string)
    return result

def get_list_single_entry_nums_by_set(output_string):
    return [set(output_string)]

def get_list_single_entry_nums(input_list):
    '''
    Возвращает список неповторяющихся элементов исходного списка 
    '''
    result = []
    if len(input_list) > 1:
        for i, item in enumerate(input_list):
            if item not in result:
                result.append(item) # result.append(input_list[i])
    elif len(result) ==  1:
        result = input_list
    return result

def get_list_many_entry_nums(input_list):
    '''
    Возвращает список повторяющихся элементов исходного списка 
    '''
    result = []
    # формируем список с неповторяющимися элементами
    list_with_single_entry = get_list_single_entry_nums(input_list)
    # ищем количество вхождений
    if len(input_list) > 1:
        for i, item_searched  in enumerate(list_with_single_entry):
            count_of_entry = 0
            for i, item in enumerate(input_list):
                if item == item_searched:
                    count_of_entry +=1
            if count_of_entry > 1 and item_searched not in result:
                result.append(item_searched) # result.append(input_list[i])
    return result

### ********* основной код - функция main  ********* 
output_string = "\nВведите список через пробел и нажмите enter: \n список -> "
list_of_nums = input_list_of_nums(output_string)
list_single_entry = get_list_single_entry_nums(list_of_nums)
list_many_entry = get_list_many_entry_nums(list_of_nums)
print(f"Результат:\n{list_of_nums}=> \
        неповторяющиеся {sorted(list_single_entry)} + \
        повторяющиеся {sorted(list_many_entry)}")