num1 = 10

num2 = 20

temp = num1 

num1 = num2

num2 = temp

print(num1,num2)


num1=10

num2 = 20 

num1,num2=num2,num1

print(num1,num2)


def prime(num1):
    if num1<=1:
        return 'not adequate number'
    
    for i in range(2,int(num1**0.5)+1):
        
        if num1%i==0:
            return 'composit number'
    return 'prime number'
print(prime(13))
print(prime(14))
print(prime(15))
print(prime(20))
print(prime(-5))


def palindrome(str1):
    
    if len(str1)<1:
        return 'input invalid'
    str2 = str1[::-1]
    if str1==str2:
        return 'palindrome'
    return 'not palindrome'
print(palindrome(''))



def palindrome(num1):
    if num1<1:
        return 'invalid number'
    rev=0
    temp=num1
    while temp>0:
        rem = temp%10
        
        rev = rev*10+rem
        
        temp=temp//10
    if rev == num1:
        return 'palindrome'
    return 'not palindrome'
print(palindrome(121))