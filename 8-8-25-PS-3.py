num1=int(input("enter a number:"))
flat=0
for i in range(2,num1):
    if num1%i==0:
        flag=1
        break
if flag==1:
    print("Not prime number")
else:
    print("prime number")
    
num1=int(input("enter a number:"))
for i in range(num1,0,-1):
    print(i)
    
num1=int(input("enter a number:"))
sum_digit=0
rem=0
while num1>0:
    rem=num1%10
    sum_digit+=rem
    num1=num1//10
print(sum_digit)

num1=int(input("enter a number:"))
product=1
rem=0
while num1>0:
    rem=num1%10
    product=product*rem
    num1=num1//10
print(product)



num1=int(input("enter a number:"))
original=num1
sum=0
rem=0
while num1>0:
    rem=num1%10
    cube=rem**3
    num1=num1//10
    sum=sum+cube
print(sum)
if sum==original:
  print("armstrong number")
else:
  print("not armstrong number")
  
  
num1=int(input("enter a number:"))
rem=0
rev=0
while num1>0:
    rem=num1%10
    rev=rem
    num1=num1//10
    print(rev,end="")
    
num1=int(input("enter a number:"))
original=num1
rem=0
rev=0
digit=0
while num1>0:
    rem=num1%10
    rev=rev*10+rem
    num1=num1//10
print(rev)
if rev==original:
    print("it is palindrome")
else:
    print("it is not palindrome")
    
    
str1="apple"
vowels=['a','e','i','o','u']
count=0
for char in str1:
    if char in vowels:
       count+=1
print(count)

str1="apple"
vowels=['a','e','i','o','u']
count=0
for char in str1:
    if char not in vowels:
       count+=1
print(count)

# 24. Count Vowels and Consonants
# Question: Count vowels and consonants in input string. Explanation: Maintain two counters. - Input: “apple” - Output: Vowels = 2, Consonants = 3

str1="apple"
vowels=['a','e','i','o','u']
vowel_count=0
cons_count=0
for char in str1:
    if char in vowels:
      vowel_count+=1
    elif char not in vowels and char.isalpha():
      cons_count+=1
print(vowel_count)
print(cons_count)


num1=int(input("enter a number:"))
sum=0
for i in range(1,num1):
    if num1%i==0:
        sum+=i
print(sum)
if sum==num1:
    print("perfect number")
else:
    print("not perfect number")
    
    
num1=int(input("enter a number:"))
sum=0
rem=0
sqrt=num1**2
while sqrt>0:
    rem=sqrt%10
    sum+=rem
    sqrt=sqrt//10

if sum==num1:
    print("neon number")
else:
    print("not neon")
    
    
    
import math
num1=int(input("enter a number:"))
original=num1
factorial=1
sum=0
rem=0
while num1>0:
  rem=num1%10
  sum+=math.factorial(rem)
  num1=num1//10
if sum==original:
    print("it is strong number")
else:
    print("it is not strong number")
    

num1=int(input("enter a number:"))
sum=0
while num1>0:
    rem=num1%10
    sum+=rem
    num1=num1//10
if num1%sum==0:
    print("harshad number")
else:
    print("Not Harshad Number")
    
    
num1=int(input("enter a number:"))
n1,n2=0,1
print("fibonacci series",n1,n2,end=" ")
for i in range(2,num1):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end=" ")
print()


    

   

    


    
    


    
    
    