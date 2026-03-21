
n1,n2=0,1
for i in range(10):
   print(n1,end=" ")
   n1,n2=n2,n1+n2
   
def prime(num1):
    for i in range(2,num1):
        if num1%i==0:
            return 'not prime'
    return 'prime'
print(prime(3))


num1=int(input('enter a num:'))
fact=1
i=1
while i<=num1:
    fact=fact*i
    i+=1
print('factorial is :',fact)

def reverse(num1):
    rev=0
    while num1>0:
        rem=num1%10
        rev=rev*10+rem
        num1=num1//10
    return rev
print(reverse(134))


def palindrome(num1):
    rev=0
    temp=num1
    while temp>0:
        rem=temp%10
        rev=rev*10+rem
        temp//=10
    if rev==num1:
        return 'palindrome'
    return 'not palindrome'
print(palindrome(1241))
