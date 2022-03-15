import random

roll = random.randomint(1, 6)

guess = int(input('Guess the dice roll:\n'))

if guess == roll:
   print('Correct! ')
else:
   print('Wrong! ')
print('The computer rolled a ' + str(roll))
