def binary_search(list1,search_ele):
    
    list1.sort()
    low = 0
    high = len(list1)-1
    
    while low <= high:
        mid = (low+high)//2
        if list1[mid] == search_ele:
              return list1[mid]
        elif list1[mid] > search_ele:
              high = mid -1
        else:
            low = mid + 1
    return 'element not found'
print(binary_search([10,20,30,40,50],50)) 


def bubble_sort(list1):
    
    n = len(list1)
    
    for i in range(n-1):
        for j in range(0,n-1-i):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
    return list1
print(bubble_sort([10,30,20,40,50,60]))