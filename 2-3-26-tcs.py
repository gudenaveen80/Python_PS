def palindrome(start,end):
    for i in range(start,end):
        num1 = i
        rev = 0
        while num1> 0:
            rem = num1 % 10 
            rev = rev *10 + rem
            num1//=10
        if i == rev:
           print(i)
palindrome(100,125)


def perfect(num1):
    sum = 0
    for i in range(1,num1//2+1):
        if num1%i ==0:
            sum+=i
    if sum == num1:
        return 'perfect number'
    return 'not perfect number'
print(perfect(6))


def prime_factors(num1):
    
    for i in range(2,num1):
        if num1%i==0:
            print(i)
            num1 = num1//i
prime_factors(12)



import math

def is_strong(num1):
    
    temp = num1
    sum_factor=0
    while temp >0:
        rem = temp%10
        sum_factor += math.factorial(rem)
        temp//=10
    return sum_factor == num1
print(is_strong(145))


def automorphic(num1):
    square = num1**2
    return str(square).endswith(str(num1))
print(automorphic(5))
print(automorphic(76))



def harshad(num1):
    temp = num1
    sum_digits=0
    while temp>0:
        rem = temp%10
        sum_digits += rem
        temp//=10
    if (num1%sum_digits==0):
        return 'harshad number'
    return 'not harshad'
print(harshad(81))
print(harshad(1729))
print(harshad(18))


def abundant(num1):
    sum = 0
    for i in range(1,num1):
        if num1%i == 0:
            sum += i
    return sum > num1
print(abundant(12))
print(abundant(15))


def gcd(a,b):
    while b!=0:
        a, b = b, a%b
    return a
print(gcd(12,18))



def gcd(a,b):
    while b!=0:
        a, b = b ,a%b
    return a
def lcm(a,b):
    return a*b // gcd(a,b)
print(lcm(12,18))
print(lcm(14,18)) 

binary ='1011'

octal = int(binary,8)
print(octal)

hexa = int(binary,16)
print(hexa)  