class Solution(object):
    def countConsistentStrings(self, allowed, words):
        result = 0
        for i in words:
            check = True
            for j in i:
                if j not in allowed:
                    check=False
            if check:
                result+=1        
                    
        return result        