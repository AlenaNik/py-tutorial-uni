weight = input('Enter your weight: ')
measure = input("The measure you've put here is (L)bs or (K)kg?  ")

if measure == 'L' or 'l':
    print(f'{int(weight) * 2.205} you weight in kg')
elif measure == 'K' or 'k':
    print(f'{int(weight) / 2.205} you weight in lbs')
else:
    print('To bien')