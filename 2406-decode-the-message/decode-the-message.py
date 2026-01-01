class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
            
        mapping = {}
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        id = 0
        
        for ch in key:
            if ch != ' ' and ch not in mapping:
                mapping[ch] = alphabet[id]
                id+= 1
        

        result = []
        for ch in message:
            if ch == ' ':
                result.append(' ')
            else:
                result.append(mapping[ch])
        
        return ''.join(result)