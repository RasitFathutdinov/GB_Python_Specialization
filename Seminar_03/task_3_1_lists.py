'''
Задача 1

Дан список повторяющихся элементов. 

Вернуть список с дублирующимися элементами. 
В результирующем списке не должно быть дубликатов.
'''
def input_list_of_nums(output_string):
    '''
    Данный метод рекурсивно предлагает пользователю корректно ввести список
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
    '''
    Возвращает список неповторяющихся элементов исходного списка (без дубликатов)
    Решение через множество
    '''
    return [*set(output_string)]

def get_list_single_entry_nums(input_list):
    '''
    Возвращает список неповторяющихся элементов исходного списка (без дубликатов)
    Решение через списки
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
    Возвращает список повторяющихся элементов исходного списка (список дубликатов)
    '''
    result = []
    # формируем список с неповторяющимися элементами (без дубликатов)
    list_with_single_entry = get_list_single_entry_nums(input_list)
    # ищем количество вхождений и формируем список (математически множество) с повторяющимися элементами 
    if len(input_list) > 1:
        for i, item_searched  in enumerate(list_with_single_entry):
            count_of_entry = 0
            for i, item in enumerate(input_list):
                if item == item_searched:
                    count_of_entry +=1
            if count_of_entry > 1 and item_searched not in result: #Условие "and item_searched not in result" убирает повторы дубликатов
                result.append(item_searched) # result.append(input_list[i])
    return result

### ********* основной код - функция main  ********* 
output_string = "\nВведите список через пробел и нажмите enter: \n список -> "
list_of_nums = input_list_of_nums(output_string)
list_single_entry = get_list_single_entry_nums(list_of_nums)   # В результирующем списке не должно быть *дубликатов* (решение не используя множества)
# list_single_entry_by_set = [*set(list_of_nums)]                   # решение через множество
list_many_entry_items = get_list_many_entry_nums(list_of_nums) # Вернуть список с дублирующимися элементами
print(f"Результат:\n{list_of_nums} => \
        \n список без дубликатов {sorted(list_single_entry_by_set)} \
        \n список с дублирующимися элементами {sorted(list_many_entry_items)}")