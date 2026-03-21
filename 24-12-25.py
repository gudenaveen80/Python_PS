n=7

for i in range(n):
    curr=1
    for sp in range(n- i- 1):
        print(' ',end='')
        
    for j in range(n):
        if i>=j:
            print(curr,end=' ')
            curr+=1
        else:
            print(' ',end=' ')
            
    print()
    
    # def leap_year(year):
    # if (year%400 == 0) or ((year%4 == 0 )and (year%100!=0)) :
    #     return 'leap year'
    # return 'not leap year'
    # print(leap_year(2000))


# def vowel_consonant(char):
#     if char.isalpha():
#         if char in 'aeiou':
#             return 'vowel'
#         elif char not in 'aeiou':
#             return 'consonant'
#     return 'neither'
# print(vowel_consonant('1').lower())
        
def vowel_consonant(char):
    return 'vowel' if char in 'aeiou' else 'consonant' if char.isalpha() else 'neither' 
print(vowel_consonant('a').lower())

       
 