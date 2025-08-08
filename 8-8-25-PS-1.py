amount=int(input("enter a amount:"))
a=amount//1000
rem_a=amount%1000
b=rem_a//500
rem_b=rem_a%500
print("1000s are:",a)
print("500s are:",b)
print("remaining",rem_b)


seconds=5000
hours=seconds//(60*60)
rem_min=seconds-(60*60)
min=rem_min//60
sec=rem_min%60
print("hours:","min:","sec:",hours,min,sec)