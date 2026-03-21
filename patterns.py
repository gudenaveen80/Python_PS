n=6

for i in range(n-1):
    for j in range(n-1):
        if j<i:
            print("",end=' ')
        else:
            print('*',end=' ')
    print()
    
    
n =7

for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    
    
    n =7

for i in range(n):
    for j in range(n):
        if i>j or i==j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    
    
n =7

for i in range(n):
    for j in range(n):
            print('*',end=' ')
    print( )
    
    
n = 7

for i in range(n):
    for j in range(n):
        if (i <= n//2 and (j <= i or j >= n-1-i)) or \
           (i > n//2 and (j <= n-1-i or j >= i)):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
    
n = 7

for i in range(n):
    for j in range(n):
        if j<n-i:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
    
    
n = 7

for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1 or i==0 or i==n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
    
    
n = 7

for i in range(n):
    for j in range(n):
        if j>=n-i:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

n = 7
print()
for i in range(n):
    for j in range(n):
        if i+j==n-1 or j==n-1 or i==n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
    
n = 7

for i in range(n):
    for j in range(n):
        if j>=i:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
    
    
n = 7

for i in range(n):
    for j in range(n):
        if j<n-i:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()






n = 7

for i in range(1,n):
    for j in range(n):
        if j<i:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
    

# 23-02-16
n = 5 

for i in range(n):
    for j in range(n):
        if i>=j:
            print('*',end=' ')
        else:
            print(' ',end='')
    print()
    
    
n = 5 

for i in range(n):
    for j in range(n):
        if j<=n-i-1:
            print('*',end=' ')
        else:
            print(' ',end='')
    print()
    
    
n=5

for i in range(1,n+1):
    
    for j in range(n-i):
        print('',end='')
        
    for k in range(i):
        print("*",end='')
    print()




