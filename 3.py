import random


rows = 4
cols = 10
min_val = -100
max_val = 100

random_matrix = [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]
print(random_matrix)

sorted_list = []

for i in range(rows):
    for j in random_matrix[i]   :
        if j > 0 :
            sorted_list.append(j)
print(random_matrix)
print(sorted_list)
