
class Solution(object):
    def findWordsContaining(self, words, x):
        a = []
        for i, word in enumerate(words): 
            if x in word:
                a.append(i) 
        return a            


            
        