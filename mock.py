num1 = 0
try:
    res=num1/0
except ZeroDivisionError:
    print('not divide by zero')

else:
    print('this excutes if all fine')

finally:
    print('this is must executed block man')

list1 =  [1,2,3]

one = iter(list1)

print(next(one))

print(next(one))

print(next(one))   
    
    