def palindrome(str1):
    rev = ''
    for ch in str1:
        rev = ch + rev
    
    if rev == str1:
        return 'palindrome'
    return 'not palindrome'
print(palindrome('LEVELA'))


def palindrome(str1):
    str2 =str1[::-1]
    if str2 == str1:
        return 'palindrome'
    return 'not palindrome'
print(palindrome('madam'))


def remove_char(str1):
    str2=''
    for ch in str1:
        if  ch.isalpha():
            str2+=ch
    return str2
print(remove_char(' naveen@123'))

def sum_str(str1):
    sum_str = 0
    for ch in str1:
        sum_str += int(ch)
    return int(sum_str)
print(sum_str('1232')) 


def capitalize_first_last(text):
    words = text.split()  # split string into words
    new_words = []

    for word in words:
        if len(word) == 1:
            new_words.append(word.upper())  # single-letter word
        else:
            # capitalize first and last character, keep middle unchanged
            new_word = word[0].upper() + word[1:-1] + word[-1].upper()
            new_words.append(new_word)

    return ' '.join(new_words)

text = "hello world python"
print(capitalize_first_last(text)) 



def non_repeating(str1):
    for ch in str1:
        if str1.count(ch)==1:
            print(ch,end=' ')
    return None
        
non_repeating('naveen')


def largest(str1):
    words = str1.split()
    max_word = max(words,key=len)
    print(max_word)
largest('naveen gude was born in warangal')


def largest_word(str1):
    words = str1.split()
    largest = ''
    for sub in words:
        if len(sub) > len(largest):
            largest = sub
    return largest
print(largest_word('naveen in hyderabad '))


def count_words(str1):
    total_words=0
    
    words = str1.split()
    for word in words:
        total_words +=1
    return total_words
print(count_words('naveen gude is born on '))


def change_case(str1):
   return str1.swapcase()
print(change_case('navEEn'))

def change_case(str1):
    result = ''
    
    for ch in str1:
        if ch.isupper():
            result+=ch.lower()
        elif ch.islower():
            result+=ch.upper()
    return result
print(change_case('NaVeeN'))





def count_cases(str1):
    uppercase=0
    lowercase=0
    digit=0
    for ch in str1:
        if ch.isupper():
            uppercase+=1
        elif ch.islower():
            lowercase+=1
        else:
            digit+=1
    return uppercase,lowercase,digit
print(count_cases('navEEn123'))



def concatenate(a,b):
   a= input('enter a str:')
   b = input('enter a str:')
   return a+b
print(concatenate(a,b))


def reverse_words(str1):
    words = str1.split()
    
    reverse_words = words[::-1]
    return ' '.join(reverse_words) 
print(reverse_words('naveen gude'))