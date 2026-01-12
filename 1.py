import random
N = random.randint(5,10)
list_of_numbers = []

for i in range (N):
    list_of_numbers.append(random.randint(1,100))
print(list_of_numbers)
biggest_digit = list_of_numbers[0]
for i in list_of_numbers:
    if i > biggest_digit:
        biggest_digit = i
print(biggest_digit)
