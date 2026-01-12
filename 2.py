import random


rows = 4
cols = 10
min_val = 1
max_val = 100

random_matrix = [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]
print(random_matrix)

biggest_summ = 0
list_summ_nested_list = []


for i in range(rows):
    summ_nested_list = 0
    for j in random_matrix[i]:
        summ_nested_list += j
    list_summ_nested_list.append(summ_nested_list)
    if summ_nested_list > biggest_summ:
        biggest_summ = summ_nested_list


print(f"""Сумма элементов каждой подстроки:""", *list_summ_nested_list, sep='\n')
print(f"""Общая сумма всех элементов {sum(list_summ_nested_list)}
Подстрока с наибольшей суммой {biggest_summ}""")
