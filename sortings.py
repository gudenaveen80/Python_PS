
def linear_search(list1,search):
    for i in list1:
        if i==search:
           return f"element is found {i}"
    return "element is not found"
     
print(linear_search([10,20,30,40],20))



def binary_search(arr1,key):
    low=0
    high=len(arr1)-1
    while low<=high:
            mid=(low+high)//2
            if arr1[mid] == key:
                return 'element found'
            elif arr1[mid] < key:
                low=mid+1
            else:
                high=mid-1
        
    return 'elements not found in array'
print(binary_search([10,20,30,40,50],20))


def bubble_sort(arr1):
    n=len(arr1)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr1[j]>arr1[j+1]:
                arr1[j],arr1[j+1]=arr1[j+1],arr1[j]
    return arr1
print(bubble_sort([10,40,20,50,60,70]))



def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr
print(selection_sort([10,40,20,30,50]))


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr
print(insertion_sort([10,30,20,60,50]))



def bubble_sort(list1):
    
    n = len(list1)
    
    for i in range(n-1):
        for j in range(0,n-1-i):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
    return list1
print(bubble_sort([10,30,20,40,50,60]))