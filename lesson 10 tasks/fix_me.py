import math, random
from math import pi
from math import e
print=5
СoUnt = int ( input ( ' Введите количество повторов : ' ) )
print ( print*СoUnt )
print ( pi*print*СoUnt )
print ( e*2 )
while     print>=0     :
        print-=1
str='my string'
sum=0
for     elem    in  str  :
        sum+=pow(str.find(elem),2)
            print ("sum=",sum)
def  MY_FUNC  (atr = 1)    :
        print ( ' atr',atr )
print ( MY_FUNC ( atr = 5 ) )




from math import pi
from math import e

print_int = 5
count = int(input('Введите количество повторов: '))
print(print_int * count)
print(pi * print_int * count)
print(e * 2)
while print_int >= 0:
    print_int -= 1
my_str = 'my string'
summa = 0
for elem in my_str:
    summa += pow(my_str.find(elem), 2)
print("summa =", summa)


def my_func (atr = 1):
    print('atr', atr)


print(my_func(atr = 5))