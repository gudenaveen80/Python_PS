def sum_digits(num1):
    sum=0
    while num1>0:
        rem=num1%10
        sum+=rem
        num1//=10
    print(sum)
sum_digits(567)

def reverse(num1):
    rev=0
    temp=num1
    while temp>0:
        rem=temp%10
        rev=rev*10+rem
        temp//=10
    return rev
print(reverse(765))


def factorial(num1):
    fact=1
    for i in range(num1):
        fact+=fact*i
    return fact
print(factorial(3))
print(factorial(10))



def middle_word(value):
    s=str(value)
    length=len(s)
    mid=length//2
    for i in s:
        if length%2==0:
            return s[mid-1]+s[mid]
        else:
            return s[mid]
    
    
print(middle_word('wonder'))
    
print(middle_word('world'))
    
print(middle_word(6969))


def sum_array(array1):
    sum=0
    for i in array1:
        sum+=i
    print(sum)
sum_array([1,2,3,4])



def largest_element(array1):
    largest=array1[0]
    for num in array1:
        if num>largest:
            largest=num
            
    return largest
print(largest_element([1,2,3,4]))



def smallest_element(array1):
    smallest=array1[0]
    for num in array1:
        if num<smallest:
            smallest=num
            
    return smallest
print(smallest_element([1,2,3,4]))

def duplicates_array(array1):
    array2=[]
    for num in array1:
        if num not in array2:
             array2.append(num)
    return array2
print(duplicates_array([1,2,3,2,4,1,1,1]))


def array_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True
print(array_sorted([4,2,3,4]))


def reverse(arr):
    arr2=[]
    for num in arr:
        arr2=[num]+arr2
    return arr2
print(reverse([2,3,4,6,7,8,9]))


def even_numbers(arr):
    sum=0
    for num in arr:
       if num%2==0:
           sum=num+sum
    return sum
print(even_numbers([1,2,3,4,5]))


def count_vowels(str1):
    count=0
    for ch in str1.lower():
        if ch in 'aeiou':
            count+=1
    return count
print(count_vowels("hello world"))


def remove_vowels(str1):
    str2=''
    for ch in str1.lower():
        if ch not in 'aeiou':
            str2+=ch
    return str2
            
print(remove_vowels("hello world"))

def rotate_array(arr1,s):
    n = len(arr1)
    s = s%n
    return arr1[-s:]+arr1[:-s]
print(rotate_array([1,2,3,4,5],3))


def inter_array(arr1,arr2):
    intersect_ele=[]
    for i in arr1:
        if i in arr2:
            intersect_ele.append(i)
    return intersect_ele
            
print(inter_array([1,2,3,4],[1,5,6,7,4,2]))




def missing_values(arr1):
    for i in range(len(arr1)-1):
        if arr1[i+1] != arr1[i]+1:
            
            return arr1[i]+1
        
            
print(missing_values([1,3,4,5,6]) )




def pair_sum(arr1,target):
    watch = set()
    
    pairs=[]
    
    for num in arr1:
        compliment = target - num
        
        if compliment in watch:
            pairs.append([num,compliment])
        watch.add(num)
    return pairs
   
print(pair_sum([0,2,4,3,1,5],5)) 





def find_peak(arr1):
    peak=None
    n = len(arr1)
    if n==1 or arr1[0] >= arr1[1]:
      peak = arr1[0]
        
    for i in range(1, n-1):
        
        if arr1[i] >= arr1[i-1] and arr1[i] >= arr1[i+1]:
            peak =  arr1[i]
    if arr1[n-1] >= arr1[n-2]:
        peak =  arr1[n-1]
    return peak
print(find_peak([1,2,3,4,10,0,15]))


def first_dup(arr1):
    seen = set()
    
    for i in arr1:
        if i in  seen:
            return i
        seen.add(i)
    return None
print(first_dup([1,2,3,4,5,2]))

        