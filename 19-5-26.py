def target_variable(arr1,target):
    n = len(arr1)
    result = []
    for i in range(n):
        for j in range(i+1,n):
            if arr1[i] + arr1[j] == target:
                result.append(arr1[i],arr1[j])
    return result
print(target_variable([1,2,3,4,5,6,7],7))


def k_positions(list1,k):
    length = len(list1)
    k = k % length
    return list1[-k:] + list1[:-k]
print(k_positions([1,2,3,4,5,6],4))



def remove_duplicate(list1):
    result = []
    for num in list1:
        if num not in result:
            result.append(num)
    return result
print(remove_duplicate([1,2,3,4,5,5,6,1,2]))


def frequency(list1):
    freq = {}
    for num in list1:
         freq[num] = freq.get(num,0) +1
    return freq
print(frequency([1,2,3,4,5,2,3,4]))



def largest_word(str1):
    largest = ''
    words = str1.split() 
    for sub in words:
        if len(sub)>len(largest):
            largest = sub
    return largest
print(largest_word('naveen gude lives in hyderabad '))


def count_words(str1):
    count_words=0
    words = str1.split()
    for sub in words:
        count_words+=1
    return count_words
print(count_words('this is naveen gude lives in hyderabad'))


def change_case(str1):
    result = ''
    for ch in str1:
        if ch.isupper():
            result+=ch.lower()
        elif ch.islower():
            result+=ch.upper()
    return result
print(change_case('naveen'))


def count_case(str1):
    lower=0
    upper=0
    digit=0
    for ch in str1:
        if ch.isupper():
            upper+=1
        elif ch.islower():
            lower+=1
        elif ch.isdigit():
            digit+=1
    return upper,lower,digit
print(count_case('Naveen123'))


def anagrams(str1,str2):
    if sorted(str1) == sorted(str2):
        return 'anagrams'
    return 'not anagrams'
print(anagrams('triangle','integral'))


def vowel_count(str1):
    vowels=0
    consts=0
    for ch in str1:
        if ch.isalpha() and ch in 'aeiou':
            vowels+=1
        else:
            consts+=1
    return vowels,consts
print(vowel_count('naveen'))



def reverse_array(list1):
    
    left = 0
    right = len(list1)-1
    while left < right :
        list1[left], list1[right] = list1[right],list1[left]
        left+=1
        right-=1
    return list1
print(reverse_array([1,2,3,4,5,6,7]))


def largest_num(list1):
    largest = list1[0]
    for num in list1:
        if num > largest:
            largest = num
    return largest
print(largest_num([1,2,3,4,5,6,7]))

def smallest_num(list1):
    smallest=list1[0]
    for num in list1:
        if num <smallest:
            smallest=num
    return smallest
print(smallest_num([1,2,3,0,4,5,6,7,0,-1]))



def second_largest(list1):
    fm = max(list1[0],list1[1])
    sm = min(list1[0],list1[1])
    for i in list1:
        if i > fm:
            sm = fm
            fm = i
        elif i > sm:
            sm = i
    return sm,fm
print(second_largest([1,2,3,4,5,6,7]))



def reverse(list1):
    rev=[]
    for num in list1:
        rev = [num] +rev
    return rev
print(reverse([1,3,4,4,5,6]))