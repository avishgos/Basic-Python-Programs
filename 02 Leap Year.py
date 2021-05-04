#using user input
num = int(input('Enter a number'))

if num % 4 == 0:
    if num % 100 == 0:
        if num % 400 == 0:
            print('Leap Year')
        else:
            print('Not a Leap Year')
    else:
        print('Leap Year')

else:
    print('Not a Leap Year')


#using definition
def checkLeap(num):
    if num % 4 == 0:
        if num % 100 == 0:
            if num % 400 == 0:
                print('Leap Year')
            else:
                print('Not a Leap Year')
                
        else:
            print('Leap Year')
    else:
        print('Not a Leap Year')

checkLeap(2000)

