numbers = [67, 2, 3, 4, 7, 8, 1, 2, 3, 4]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print(largest)