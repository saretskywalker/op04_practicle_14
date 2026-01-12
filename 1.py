import random
N = random.randint(5,10)
list_of_numbers = []
list_of_numbers_2 = []

for i in range (N):
    list_of_numbers.append(random.randint(1,100))
print(list_of_numbers)

for i in range (N):
    list_of_numbers_2.append(random.randint(1,100))
print(list_of_numbers_2)

list_of_numbers = [list_of_numbers_2, list_of_numbers]
print(list_of_numbers)

biggest_digit = list_of_numbers[0][0]
index_biggest_digit =f"{0} {list_of_numbers[0].index(biggest_digit)}"

for i in range(len(list_of_numbers)):
    for j in list_of_numbers[i]:
        if j > biggest_digit:
            biggest_digit = j
            index_biggest_digit =f"{i} {list_of_numbers[i].index(biggest_digit)}"

print(f"Наибольший элемент списка: {biggest_digit} позиция элемента в списке{index_biggest_digit}")
