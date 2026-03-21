def vowels(word):
    n=word.lower()
    rev=''
    for i in n:
        if i in 'aeiou':
           rev+=i
           print(rev[::-1])
           
vowels('helloworld')


def vowels(word):
    return ''.join(i for i in word if i.lower() in 'aeiou')[::-1]

print(vowels('JackSpaArrow'))



def vowels(word):
    str1=''
    for i in word.lower():
        if i in 'aeiou' and i not in str1:
            str1+=i
    print(str1)

vowels('Jacksparrow')


def duplicates_removal(word):
    str1=''
    for i in word.lower():
        if i not in str1:
            str1=str1+i
    print(str1)
duplicates_removal('madam')


def duplicates_removal_original (word):
    str1=''
    for ch in word.lower():
        if word.count(ch) == 1:
            str1+=ch
    print(str1)
duplicates_removal_original('donkey')


def toggle_case(word):
    str1=''
    for ch in word:
        if ch.isupper():
            str1+=ch.lower()
        elif ch.islower():
            str1+=ch.upper()
        else:
            str1+=ch
    print(str1)
toggle_case('JohnWick')
toggle_case('koRean')


def check_sum(num1):
    n=str(num1)
    first_last_sum=int(n[0])+int(n[-1])
    middle=0
    for i in n[1:-1]:
        middle+=int(i)
    if middle==first_last_sum:
        return 'equal'
    return 'not equal'
print(check_sum(75547))


def check_greater(num1):
    n=str(num1)
    first=int(n[0])
    last=int(n[-1])
    for s in n[1:-1]:
        if int(s)>=first or int(s)>=last:
            return 'false'
        return 'true'
print(check_greater(84719))


def min_max_first(num1):
    n = str(num1)
    first = int(n[0])
    
    # check if min is first
    is_min = True
    for i in n[1:]:
        if int(i) < first:   # if any digit is smaller than first
            is_min = False
            break
    if is_min:
        return 'min is first'
    
    # check if max is first
    is_max = True
    for i in n[1:]:
        if int(i) > first:   # if any digit is greater than first
            is_max = False
            break
    if is_max:
        return 'max is first'
    
    return 'neither min nor max'

print(min_max_first(6381))  # min is first
print(min_max_first(7198))  # max is first
print(min_max_first(4267))  # neither min nor max

def str1_to_num(str1):
    for i in str1:
        print(int(i),end='')
str1_to_num('123')

def only_num(str1):
    for i in str1:
        if not i.isdigit() :
            return False
    return True
print(only_num('1234'))


def count_occurance(str1,ch):
    count=0
    for i in str1:
        if i==ch:
            count+=1
    return count
print(count_occurance('hello world','l'))


def falsy_values(arr1):
    arr2=[]
    for i in arr1:
        if i:
            arr2.append(i)
    return arr2
print(falsy_values([0,1,False,2,'',3]))


def reverse_capital(str1):
    str2=''
    str3=''
    for i in str1:
        if i.isupper():
            str2=i+str2
        else:
            str3=i+str3
    return str2+str3
print(reverse_capital('OnavNeen'))


def second_largest(arr1):
    f_max=max(arr1[0],arr1[1])
    s_max=min(arr1[0],arr1[1])
    for num in range(2,len(arr1)):
        if num>f_max:
            f_max=num
            s_max=f_max
        elif num>s_max:
            s_max=num
    return s_max
print(second_largest([1,2,3,4,5,6,7,8]))





def second_smallest(arr1):
    f_min = min(arr1[0], arr1[1])
    s_min = max(arr1[0], arr1[1])

    for num in arr1[2:]:
        if num < f_min:
            s_min = f_min
            f_min = num
        elif num < s_min:
            s_min = num

    return s_min


print(second_smallest([1, 2, 3, 4, 5, 6, 7, 0, -1]))
