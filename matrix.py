# n=[[1, 1, 1],
#   [2, 2, 2],
#   [3, 3, 3]
# ]
# transpose=list(zip(*n))
# for row in transpose:
#     print(row)


list1=[[1,2,3],
   [1,2,3],
   [1,2,3]
]
size=len(list1)
for i in range(size):
    for j in range(size):
        if i>j:
            list1[i][j],list1[j][i]=list1[j][i],list1[i][j]
for row in list1:
    print(row)
    
    
list1=[[1,2,4],
   [1,2,3],
   [1,2,3]
]
n=len(list1)
outer_sum=0
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            outer_sum+=list1[i][j]
print('outer_sum',outer_sum)



list1=[[7,2,4],
   [1,2,3],
   [1,2,3]
]
n=len(list1)
diagonal_sum=0
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            diagonal_sum+=list1[i][j]
print('diagonal_sum',diagonal_sum)



list1=[[7,2,4],
   [1,2,3],
   [1,2,3]
]
n=len(list1)
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print(list1[i][j],end=' ')
        else:
            print('',end='  ')
    print()
    
    
list1=[[8,1,3],
     [4,2,9],
     [3,1,5]
    ]
n=len(list1)
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print(list1[i][j],end=' ')
        else:
            print('',end=' ')
    print()  
    
list1=[[1,2,3],
     [4,5,3],
     [2,5,3]
    ]
n=len(list1)
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print(list1[i][j],end=' ')
        else:
            print(' ',end='')
    print()
    
list1=[[1,2,3],
     [4,5,3],
     [2,5,3]
    ]
n=len(list1)
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or j==n-1 or i==n-1:
            print(list1[i][j],end=' ')
    
    