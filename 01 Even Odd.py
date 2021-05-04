#using  user input

num = int(input('Enter a number'))

if num%2==0:
    print('It is a even number')
else:
    print('it is a odd number')


#using definition
def Evenodd(num):
    if num%2==0:
        print('It is a even number')
    else:
        print('it is a odd number')

Evenodd(7)
