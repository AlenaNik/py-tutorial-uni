secret = 10
guess = 0
numOfGuess = 3
while guess < numOfGuess:
    res = int(input('Guess: '))
    guess += 1
    if res == secret:
        print('Nice')
        exit()
    else:
        continue