class Solution(object):
    def mostWordsFound(self, sentences):
        count = 0
        for i in sentences:
            a = 0
            for j in i:
                if j ==' ':
                    a +=1
            if a > count:
                count = a
        return count+1
                


            
                
        