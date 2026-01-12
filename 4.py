import random


rows = 4
cols = 10
min_val = 1
max_val = 100

target = random.randint(min_val, max_val)
print(target)
random_matrix = [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]
print(random_matrix)


found = False
for i in range(len(random_matrix)):
    for j in range(len(random_matrix[i])):
        if random_matrix[i][j] == target:
            print(f"Найдено в: строка {i}, позиция {j}")
            found = True

if not found:
    print("Элемент не найден")
