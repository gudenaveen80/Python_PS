def average(list1):
    length=len(list1)
    sum = 0
    avg = 0
    for num in list1:
        sum += num
        avg = sum/length
    return avg
     
print(average([1,2,3,4]))



def frequency(list1):
    freq = {}
    for num in list1:
        freq[num]=freq.get(num,0)+1
    return freq
print(frequency([1,3,2,3,1,4,4]))



def duplicates (list1):
    list2=[]
    for num in list1:
        if list1.count(num) >1 and num not in list2:
            list2.append(num)
    return list1,list2
print(duplicates([1,2,3,4,2,3,2,5]))


def duplicates_removal(list1):
    
    list2 =[]
    
    
    for num in list1:
        if num not in list2:
            list2.append(num)
            
    return list2
print(duplicates_removal([1,2,3,4,5,6,2,3,4]))



def remove_duplicates_unsorted(arr):
    result = []
      # track elements we already added
    
    for num in arr:
        if num not in result:
            result.append(num)
    
    return result

# Example
unsorted_arr = [4,2,5,2,3,4,1,5]
sorted_arr = [1,2,2,3,3,4,5,6,7]
print(remove_duplicates_unsorted(sorted_arr))




def k_rotations(list1,k):
    length = len(list1)
    
    k = k% length
    return list1[-k:] + list1[:-k]
print(k_rotations([1,2,3,4,5,6],3))




def target_pairs(arr1,target):
     
    n = len(arr1)
    
    result = []
    
    for i in range(n):
        for j in range(i+1,n):
            if arr1[i]+arr1[j]==target:
                result.append((arr1[i],arr1[j]))
    return result
print(target_pairs([1,2,3,4,5,6,7,2],7))

