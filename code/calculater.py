def add(num1,num2):
    result=num1+num2
    print('Result is: '+ str(result))

def sub(num1,num2):
    result=num1-num2
    print('Result is: '+ str(result))

def mul(num1,num2):
    result=num1*num2
    print('Result is: '+ str(result))

def div(num1,num2):
    result=num1/num2
    print('Result is: '+ str(result))

print('1. Add..')
print('2. sub..')
print('3. mul..')
print('4. div..')
print('5. exit..')

while True:
    choice=int(input('enter your choice'))
    if (choice>=1 and choice<=4):
        print('Enter two number')
        num1=int(input('enter 1st number'))
        num2=int(input('enter 2st number'))
        if choice==1:
            add(num1,num2)
        elif choice==2:
            sub(num1,num2)
        elif choice==3:
            mul(num1,num2)
        else:
            choice ==4
            div(num1,num2)
    elif choice==5:
            break
    else:
            print('somthing wrong!!!!!')
            
                 
               

