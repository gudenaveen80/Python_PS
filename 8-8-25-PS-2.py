num1=int(input("enter a number:"))
if num1%2==0 and num1%3==0 and num1%6==0:
    print("satisfy") 
    
else:
    print("it is not divisble by 6")
    
    # 7. Student Pass/Fail Based on All Subjects >= 35
# Question: Check if a student passed all subjects (maths, physics, chemistry). Explanation: Student passes only if marks in all subjects are 35 or more. - Input: Maths = 40, Physics = 36, Chemistry = 30 - Output: Fail

# sub1=int(input("enter maths:"))
# sub2=int(input("enter physics:"))
# sub3=int(input("enter chemistry:"))
# if sub1>=35 and sub2>=35 and sub3>=35:
#     print("all pass")
# else:
#     print("Fail")


# num1=int(input("enter a number:"))
# count=0
# for i in range(2,num1):
#     if num1%i==0:
#         print(i)
#         print(i**2)
# print("Perfect Square")

# import math
# Members=int(input("enter a number:"))
# cars=Members//5
# print(ceil(cars))

# num1=int(input("enter a number:"))
# num2=int(input("enter a number:"))
# num3=int(input("enter a number:"))
# if num1>num2 and num1<num3:
#   print(num1)
# elif num2>num1 and num2<num3:
#   print(num2)
# else:
#   print(num3)