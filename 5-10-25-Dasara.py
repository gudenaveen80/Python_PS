# Easy Questions...



# Check if a number is even or odd.

def even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"
print(even_or_odd(10))
print(even_or_odd(5))


# Find the maximum and minimum element in a list.

def max_and_min(list1):
   max_ele = list1[0]
   min_ele = list1[0]
   for num in list1:
       if num > max_ele:
          max_ele = num
       elif num < min_ele:
            min_ele = num
   return max_ele,min_ele
    
    
list1 = [10,70,30,40,50]
max_ele,min_ele = max_and_min(list1)
print(max_ele)
print(min_ele)




# Reverse a string without using slicing ( [::-1] ).

def rev_str(str1):
    str2 = ""
    for char in str1:
           str2 = char + str2
    return str2
    
str1 = "Hyderabad"
print(rev_str(str1))



# Check if a string is a palindrome.
def palindrome_not(str1):
    if len(str1) == 0 :
        return "invalid string"
    str2 = ""
    for char in str1:
        str2 = char + str2
    if str1 == str2:
        return "Palindrome"
    return "not palindrome"
        
str1 = "1221"
print(palindrome_not(str1))



# Find the factorial of a number (using loop).


def factorial(num1):
   if num1 < 0:
       return "invalid number"
   elif num1 == 0:
       return 1
   for i in range(1,num1):
      num1 *= i
   return num1
num1 = 4
print(factorial(num1))


# Count the frequency of each character in a string.
#first method...
def frequency_count(str1):
    freq_dict = {}
    for char in str1:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    
    return freq_dict    
    
    
str1 = "naveenkumar"
res = frequency_count(str1)
print(res)




# Find the second largest number in a list.
def second_largest(list1):
    fm = max(list1[0],list1[1])
    sm = min(list1[0],list1[1])
    for i in range(2,len(list1)):
        if list1[i] > fm:
            sm = fm 
            fm = list1[i]
        elif list[i] > sm:
             sm = list1[i]
    print("second largest is",sm)
        
list1 = [10,20,30,70,40,50]
second_largest(sorted(list1))





# Count how many vowels and consonants are in a string.


def vowel_consonant(str1):
    if len(str1) == 0 :
        return "invalid string"
    v_count = 0
    con_count = 0
    for char in str1:
        if char in "aeiouAEIOU":
            v_count += 1
        else:
            con_count += 1 
    print("v_count",v_count)
    print("con_count",con_count)
str1 = input("enter a string ")
vowel_consonant(str1)


# Calculate the sum of digits of a number.

def sum_digit(num1):
    sum = 0
    while num1 > 0:
        sum  += num1%10
        num1 = num1//10
    print(sum)
num1 = abs(int(input("enter a number to sum:")))
sum_digit(num1)


# Print the multiplication table of a number.
def multi_table(num1):
    for i in range(1,21):
       print(f"{num1} * {i} = {num1*i}")
    
num1 = int(input("enter a table "))   
multi_table(num1)


# Find the largest word in a given sentence.

def largest_word(str1):
    str2 = str1.split()
    print(str2)
    large_word = str2[1]#take it as sample case
    for word in str2:
        if len(word) > len(large_word):
            large_word = word
    print(large_word)  
str1 = "All silver Tea cups"
largest_word(str1)

# Remove all duplicate elements from a list.
def rem_duplicate(list1):
    if len(list1) == 0:
        return "invalid list"
    list2 = []
    for i in list1:
        if i not in list2:
           list2.append(i)
    print(list2)


list1 = []
print(rem_duplicate(list1))
list2 = [1,2,3,4,2,5,5,6,7]
rem_duplicate(list2)


# Sort a list without using Python’s built-in .sort() .

def sorting(list1):
    n = len(list1)
    for i in range(n):
        for j in range(0,n-i-1):
            if list1[j] > list1[j+1]:
                list1[j],list1[j+1] = list1[j+1],list1[j]
    return list1
            
list1 = [10,5,20,7,50,30,40]
print(sorting(list1))

# Merge two lists into a single sorted list.
list1 = [10,30,20,40]
list2 = [5,35,25,15]
def sorting(list3):
    n = len(list3)
    for i in range(n):
        for j in range(0,n-i-1):
            if list3[j] > list3[j+1]:
                list3[j],list3[j+1] = list3[j+1],list3[j]
    return list3
            

list3 = list1 + list2
print(sorting(list3))
# Check if a number is a prime number.

def prime_not(num1):
    if num1 == 1 or num1 == 0:
        return "invalid input"
    for i in range(2,num1//2):
        if num1%i == 0:
           return "not prime"
    return "prime"
num1 = int(input("enter a number "))
print(prime_not(num1))

# Medium (15 Questions)
# Find all pairs in a list that sum up to a target value.


# rotating list by k positions..
def rotated_list(lst,k):
    n = len(lst)
    
    k = k % n
    
    rotated_list = lst[-k:] + lst[:-k]
    
    return rotated_list





lst = [1,2,3,4,5]

k = -3
print(rotated_list(lst,k))
def miss_in_cons(list1):
    
    min1 = min(list1)
    max1 = max(list1)
    
    for i in range(min1,max1):
        if i not in list1:
            print(i)
        
list1 = [1,2,4,5,6,7,8,9]

miss_in_cons(list1)


# Check if two strings are anagrams.


str1 = "silent"
str2 = "listen"
sort_str = "".join(sorted(str1))
# print(sort_str)
sort_str2 = "".join(sorted(str2))
# print(sort_str2)
if sort_str == sort_str2:
    print("anagram")
    
    
#second method 
# Check if two strings are anagrams.
def frequency_count(str1,str2):
    if len(str1) != len(str2):
        return "not anagram"
    freq_dict1 = {}
    freq_dict2 = {}
    for char in str1:
        if char in freq_dict1:
            freq_dict1[char] += 1
        else:
            freq_dict1[char] = 1
            
    for char in str2:
        if char in freq_dict2:
            freq_dict2[char] += 1
        else:
            freq_dict2[char] = 1
    if freq_dict1== freq_dict2:
        return "anagrams"
        
    return "not anagrams"
    
    
    
str1 = "cat"
str2 = "act"
res = frequency_count(str1,str2)
print(res)
    
    
# Count the number of words in a sentence.

def words_in_sentence(str1):
    str2 = str1.split()
    return len(str2)
    
    
str1 = "my python trainer is cool."
res = words_in_sentence(str1)
print(res)


# Remove all duplicate words from a sentence.

def remove_duplicate(str1):
    words = str1.split()
    uniq_words = []
    for word in words:
        if word not in uniq_words:
            uniq_words.append(word)
    return ' '.join(uniq_words)


str1 = "naveen naveen is full stack developer"
res = remove_duplicate(str1)
print(res)



# Given a dictionary, invert it (keys become values).
dict1 = {
    1 : "naveen",
    2 : "anusha",
    3 : "shadhwin",
    4 : "bala"
}
# print(dict1)

print(dict(zip(dict1.values(), dict1.keys())))
# Find the intersection of two lists.


list1 = [1,2,3,4,5]
list2 = [6,7,8,2,3]
list3 = set(list1)
print(list3)
list4 = set(list2)
print(list4)
com_el = list3.intersection(list4)
list5 = list(com_el)
print(list5)


list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 2, 3]

intersection = list(set(list1) & set(list2))
print(intersection)


#print the matrix transpose
matrix1 = [
      [ 1 ,2 ,3 , 4  ],
      [ 5 ,6, 7 , 8  ],
      [ 9,10,11 , 12 ]
       ]
     
for j in range(len(matrix1)+1):
    for i in range(len(matrix1)):
        print(matrix1[i][j], end = " ")
    print()
# Implement bubble sort.

def bubble_sorting(list1):
    n = len(list1)
    for i in range(n):
        for j in range(0,n-i-1):
            if list1[j] > list1[j+1]:
                list1[j],list1[j+1] = list1[j+1],list1[j]
    return list1
            
list1 = [10,5,20,7,50,30,40]
print(bubble_sorting(list1))


# # # Find the first non-repeating character in a string.
from collections import Counter

def first_non_repeating(str1):
    char_count = Counter(str1)
    for char in str1:
        if char_count(char) == 1:
            return char
    return None
        
            
str1 = "swiss"
print(first_non_repeating(str1))


# Find the longest word in a sentence.

def largest_word(str1):
    str2 = str1.split()
    print(str2)
    large_word = str2[1]#take it as sample case
    for word in str2:
        if len(word) > len(large_word):
            large_word = word
    print(large_word)  
str1 = "All silver Tea cups"
largest_word(str1)



# Find the second smallest number in a list.

def second_minimum(list1):
    fm = min(list1[0],list1[1])
    sm = max(list1[0],list1[1])
    for i in range(2,len(list1)):
        if list1[i] < fm:
            sm = fm 
            fm = list1[i]
        elif list1[i] < sm and list1[i] != fm:
             sm = list1[i]
    print("second minimum is",sm)
        
list1 = [10,20,30,70,40,50]
second_minimum((list1))


# Implement a program to check if a number is an Armstrong number.
def armstrong_not(num1):
    reverse = 0
    count = len(str(num1))
    temp = num1
    
    while temp > 0:
        rem = temp % 10
        reverse +=  rem ** count
        temp //= 10
    if reverse == num1:
        return "armstrong number"
    return "not armstrong number"
num1 = int(input("enter a number "))

res = armstrong_not(num1)
print(res)
