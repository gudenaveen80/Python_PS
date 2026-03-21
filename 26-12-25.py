def reverse(num1):
    rev=0
    while num1>0:
        rem=num1%10
        rev=rev*10+rem
        num1=num1//10
    return rev
print(reverse(125)) 


def palindrome(num1):
    count=0
    rev=0
    temp=num1
    while temp>0:
        rem=temp%10
        rev=rev*10+rem
        temp=temp//10
        count+=1
    
    if rev==num1:
       print('palindrome')
    else:
       print('not palindrome')
palindrome(1221)


while True:
    inp=int(input('enter number:'))
    if inp<0:
        break
    
def fibonacci(num1):
    a,b=0,1
    for i in range(num1):
        print('current Numbers:',a,b)
        a,b=b,a+b
fibonacci(10)

def prime_not(num1):
    for i in range(2,num1//2):
        if num1%i==0:
            return 'not prime'
    return 'prime'
print(prime_not(1))


def factorial(num1):
    fact=1
    while num1>0:
        fact=fact*num1
        num1-=1
    print(fact)
factorial(5)