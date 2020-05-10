import random


secretNumber=random.randint(1,20)
print('i am currently thinking of a number')

for i in range(1,4):
    print('try to guess the number!')
    guess=int(input('Enter the number between 1 to 20')
              if guess < secretNumber:
              print('the number is low')
              elif guess>secretNumber:
                  print('the number is high')
                  else:
                      break
if guess==secretNumber:
    print('congratulation you have guess the number')
else:
    print(' better luck next time  : corecct number was '+  str(secretNumber))
