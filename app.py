try:
    age = int(input('Age: '))
    income = int(input('Income: '))
    print(age / income)
except ValueError:
    print('Enter a number')
except ZeroDivisionError:
    print('Cant be zero')