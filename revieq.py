def anagrams(word1,word2):
    word1= word1.lower()
    word2=word2.lower()
    
    if len(word1)!=len(word2):
        return False
    for i in word1:
        if word1.count(i)!=word2.count(i):
            return False
    return True
    
print(anagrams('earth','heart'))