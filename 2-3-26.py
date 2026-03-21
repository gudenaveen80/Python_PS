num1 = 10

num2 = 20

num1 = num1 + num2 

num2 = num1 - num2

num1 = num1 - num2

print(num1,num2)



def factors(num1):
    
    for i in range(1,num1+1):
        if num1%i==0:
            print(i)
factors(10)


def factorial(num1):
    
    fact = 1
    
    for i in range(1,num1+1):
        fact = fact*i
    return fact
print(factorial(5))


start =1 
end = 100

for num in range(start,end+1):
    if num > 1:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                break
        else:
            print(num)
            
def string_count(str1):
    repeat=[]
    for ch in str1:
        if str1.count(ch)>1:
            repeat.append(ch)
    print(repeat)
string_count('naveen')


num = int(input('enter a number:'))

num1 ,num2 = 0, 1

for i in range(num):
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    print('the fibonacci series :',num3)
    
    
    def vowel_count(s):
    vowels = 0
    consonants = 0
    
    for ch in s.lower():
        if ch.isalpha():   # check if character is a letter
            if ch in 'aeiou':
                vowels += 1
            else:
                consonants += 1
                
    return vowels, consonants

print(vowel_count('NAVEEN'))


def anagrams(str1,str2):
    if sorted(str1)==sorted(str2):
        return 'anagrams'
    else:
        return 'not anagrams'
print(anagrams('listen','silen'))

def anagrams(word1,word2):
    word1 = word1.replace(" ",'').lower()
    
    word2 = word2.replace(" ",'').lower()
    
    return sorted(word1) == sorted(word2)
print(anagrams('listen','silen'))


from collections import Counter

str1 = 'ravi'

freq = Counter(str1)

print(freq)


def count_occur(str1):
    freq = {}
    for ch in str1:
        freq[ch] = freq.get(ch,0)+1
    return freq
print(count_occur('naveen'))

def frequency(str1):
    
    freq={}
    
    for ch in str1:
         freq[ch] =freq.get(ch,0)+1
        
    return freq
print(frequency('virati'))



name = input('enter a name:')

char = input('enter a ch:')
count = 0
for ch in name:
    if ch == char:
        count+=1
print(count)



def two_occurance(str1):
    
    freq = {}
    
    for ch in str1:
        
        freq[ch] = freq.get(ch,0)+1
    for ch in str1:
        if freq[ch] == 2:
          print(ch)
print(two_occurance('naveen')) 


def single(str1):
    
    for ch in str1:
        if str1.count(ch)==1:
            return ch
            break
print(single('anusha'))




def missing(list1):
    n =max(list1)
    total_sum = n*(n+1)//2
    
    sum = 0
    for i in list1:
        sum+=i
    print('missing is:',total_sum-sum)
missing([1,2,3,4,6,7,8])



def repeated_ele(list1):
    list2=[]
    for num in list1:
        if list1.count(num)>1:
             list1.remove(num)
    return list1
print(repeated_ele([1,2,3,4,5,6,7,4,1,2,3]))



def del_repeat(list1):
    freq={}
    
    for num in list1:
        freq[num] = freq.get(num,0)+1
    for num in list1:
        if list1.count(num)>1:
            list1.remove(num)
    return list1
print(del_repeat([1,2,3,4,5,6,7,4,2,3]))


def largest_num(list1):
    largest = list1[0]
    for num in list1:
        
        if num > largest:
            largest = num
    return largest
print(largest_num([1,2,3,4,5,6,7]))


def smallest_num(list1):
    
   
    if not list1:
        return 'invalid input'
    smallest = list1[0]
    for num in list1:
        if num < smallest:
            smallest = num
    return smallest
print(smallest_num([]))


def second_largest(list1):
    fm = max(list1[0],list1[1])
    sm = min(list1[0],list1[1])
    for i in list1:
        if i>fm:
            sm = fm
            fm = i
            
        elif i>sm:
            sm = i
    return sm,fm
print(second_largest([1,2,3,4,5,6,7,8]))


def second_smallest(list1):
    if len(list1)<2:
        return None
    first_smallest = max(list1[0],list1[1])
    second_smallest = min(list1[0],list1[1])
    
    for i in range(2,len(list1)):
        if list1[i] < first_smallest:
            second_smallest = first_smallest
            first_smallest = list1[i]
            
        elif list1[i] < second_smallest:
            second_smallest = list1[i]
    return second_smallest, first_smallest
    
print(second_smallest([1]))





def third_largest(list1):
    if len(list1)<3:
        return None
    first_max = second_max = third_max = float('-inf')
    
    for i in list1:
        if i > first_max:
            third_max = second_max
            second_max = first_max
            first_max = i
            
        elif i > second_max and i!=first_max:
            third_max = second_max
            second_max = i
            
        elif i > third_max and i!= first_max and i!= second_max:
            third_max = i
    return third_max
    
print(third_largest([1,2,3,4,5,6]))




def third_min(list1):
    if len(list1)<3:
        return None
    
    first = second = third = float('inf')
    
    for i in list1:
        if i < first:
            third = second
            second = first
            first = i
        elif i < second and i!= first:
            third = second
            second = i
        elif i < third and i!=first and i!=second:
            third = i
    return third,second,first
print(third_min([1,2,3,4,5,6]))




def linear_search(list1,search_ele):
    for num in list1:
        if num == search_ele:
           break
    return search_ele
print(linear_search([10,20,30,40,50,60],40))    