def leap_or_not(year):
    if  year%400==0 or (year%4==0 and year%100!=0):
        return 'leap year'
    return 'not leap year'
print(leap_or_not(1700))

def day_week(day):
    if day==1:
        return 'monday'
    elif day==2:
        return 'tuesday'
    elif day==3:
        return 'wednesday'
    elif day==4:
        return 'thursday'
    elif day==5:
        return 'friday'
    elif day==6:
        return 'saturday'
    elif day==0:
        return 'sunday'
    return 'invalid day'
print(day_week(2))

def vowel_consonant(char):
    char=char.lower()
    if len(char)!=1 or not char.isalpha():
        return 'invalid input'
    elif char in 'aeiou':
        return 'vowel'
    return 'consonant'
print(vowel_consonant('@'))

def grade(marks):
    if marks<0 or marks >100:
        return 'invalid input'
    elif marks>=90 and marks<100:
        return 'A'
    elif marks>=80:
        return 'B'
    elif marks>=70:
        return 'C'
    return 'fail'
print(grade(79))
print(grade(101))

def valid_not (a,b,c):
    if a+b>c and a+c>b and c+b>a:
        return 'it is triangle'
    return 'invalid triangle'
print(valid_not(1,12,14))


num1=132
rev=0
sum_digit=0
while num1>0:
    rem=num1%10
    rev=rev*10+rem
    sum_digit+=rem
    num1//=10
print(rev,sum_digit)


num1=int(input('enter a number'))
while num1>0:
    num1=int(input('enter a number:'))
print('you have entered negative number,please stop')