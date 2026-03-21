dict1 = [1,2,3,4,5,5,6,6,7,8,9]
count={}
for num in dict1:
    if num in count:
        count[num]+=1
    else:
        count[num]=1
print(count)


dict1 = ["anu", "bala", "naveen", "shaddu"]
word_lengths = {}

for words in dict1:
    word_lengths[words] = len(words)
    
print(word_lengths)


str1 = 'naveen'

char_count = {}
     
for ch in str1:
    if ch in char_count:
        char_count[ch]+=1
    else:
        char_count[ch]=1
print(char_count)


keys=['name','age','city','edu']

values=['naveen',22,'hyd','cse']

dict1={}

for i,j in zip(keys,values):
    dict1[i]=j
print(dict1)



dict1={'naveen':22,"anusha":23,'bala':25}

list1=list(dict1.keys())
print(list1)


swap_dict={}

for key,values in dict1.items():
    swap_dict[values]=key
    
print(swap_dict)






def merge_dictionary(d1,d2):
    result = d1.copy()
    for key,values in d2.items():
        if key in result:
           result[key]+=values
        else:
            result[key]=values
    return result
    
d1 = {'a':'naveen','b':'anusha','c':'harshi'}
d2={'d':'bala','e':'venky','f':'sailu'}
print(merge_dictionary(d1,d2))



def anagrams(s1,s2):
    return sorted(s1)==sorted(s2)



s1 = 'listen'
s2 = 'silent'
print(anagrams(s1,s2))