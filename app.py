numbers = [5, 2, 5, 6, 1]
uniques = []
for num in numbers:
    if num not in uniques:
        uniques.append(num)
print(uniques)
