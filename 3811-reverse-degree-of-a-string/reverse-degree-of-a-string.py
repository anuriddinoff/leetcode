class Solution(object):
    def reverseDegree(self, s):
        total = 0
        
        for i in range(len(s)):

            position_word = i + 1
            char_position = ord(s[i]) - 96 
            reverse_position = 27 - char_position
            total += position_word * reverse_position
            
        return total