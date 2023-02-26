number = [1, 5, 3, 7, 9, 8, 2]
limit = len(number) - 1
change = 0

for i in range(limit):
    for j in range(limit):
        if number[j] > number[j + 1]:
            change = number[j + 1]
            number[j + 1] = number[j]
            number[j] = change

print(number)
