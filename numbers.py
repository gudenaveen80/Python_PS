def perfect(num1):
    sum=0
    for i in range(1,num1):
        if num1%i==0:
            sum+=i
    if sum==num1:
        return 'perfect number'
    else:
        return 'not perfect number'
print(perfect(496))


def sum_odd_digits(num1):
    sum=0
    temp=num1
    while temp>0:
        rem=temp%10
        if rem%2==1:
            sum+=rem
        temp//=10
    print(sum)
sum_odd_digits(156789)

def fibonacci(num):
    n1, n2 = 0,1

    for i in range(num):
        print(n1)
        n1, n2 = n2, n1 + n2

fibonacci(10)

print('prime numebrs btw 1 to 100 are:')
for num in range(1,101):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
       print(num,end=' ')
       
       
num1=int(input('enter a number:'))
sum=0

while num1>0:
    digits=num1%10
    count=0
    for i in range(1,digits+1):
        if digits%i==0:
            count+=1
    if count!=2:
        sum+=digits
    num1//=10
print('sum of non prime is',sum)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))

# Find the nearest smaller or equal prime
lower = num
while lower > 1:
    if is_prime(lower):
        break
    lower -= 1

# Find the nearest larger or equal prime
higher = num
while True:
    if is_prime(higher):
        break
    higher += 1

# Compare distances
if lower == higher:
    print("Nearest prime is:", lower)
elif num - lower == higher - num:
    print("Nearest primes are:", lower, "and", higher)
elif num - lower < higher - num:
    print("Nearest prime is:", lower)
else:
    print("Nearest prime is:", higher)



def amstrong(num1):
    sum=0
    temp=num1
    digits=len(str(num1))
    while temp>0:
        digit=temp%10
        sum+=digit**digits
        temp//=10
    if sum==num1:
        return 'Amstrong number'
    return 'not armstrong number'
print(amstrong(9474))


def amstrong(num1):
    sum=0
    temp=num1
    digits=len(str(num1))
    while temp>0:
        digit=temp%10
        sum+=digit**digits
        temp//=10
    return sum==num1
start=int(input('enter a starting armstrong number:'))
end=int(input('enter a starting armstrong number:'))

print('armstrong numbers are in the {start} and {end} are:')
for num in range(start,end+1):
    if amstrong(num):
        print(num,end=' ')
        
        
import copy

list1 = [1,2,[3,4]]

shallow = copy.copy(list1)

list1[0]=10

list1[2][0]=20

print(list1)
print(shallow)


import copy

list1 = [1,2,[10,30]]

deepcopy = copy.deepcopy(list1)

list1[0]=100
list1[2][0]=200

print(list1)
print(deepcopy)


def find_hcf (a,b):
    while b!=0:
        temp = a%b
        a=b
        b=temp
    return a
def find_lcm(a,b):
    hcf = find_hcf(a,b)
    return (a*b)//hcf
num1 =12
num2 = 15

print('hcf is ',find_hcf(num1,num2))
print('lcm is ',find_lcm(num1,num2))

def factorial(num1):
    
    fact = 1
    
    for i in range(1,num1+1):
        
        fact = fact * i 
        
    return fact
print(factorial(5))