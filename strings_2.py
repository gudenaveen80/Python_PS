def longest_word(sentence):
    
    
    
    words = sentence.split()
    
    
    longest=" "
    
    for word in words:
        if len(word)>=len(longest):
            longest=word
    return longest
print(longest_word('the quick brown fox jumps over the lazy dog'))




def first_non_repeat(str1):
    count = {}
    
    for ch in str1:
        count[ch]=count.get(ch, 0)+1
    for ch in str1:
        if count[ch] == 1:
            return ch
    return None
print(first_non_repeat('naveen'))


def string_compress(str1):
    
    result = ''
    count = 1
    
    for i in range(1,len(str1)):
        
        if str1[i] == str1[i-1]:
            count+=1
          
        else:
            result+=str1[i-1]+str(count)
            count=1
    result = result + str1[-1] + str(count) 
    return result
print(string_compress('aaabbbccc'))