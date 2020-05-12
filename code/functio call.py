import random



def getNumber(number):

    if number==1:
        return 'the number is 1'
    elif number==2:
        return 'the number is 2'
    elif number==3:
        return 'the number is 3'

random_number=random.randint(1,3)
pick= getNumber(random_number)
print(pick)
