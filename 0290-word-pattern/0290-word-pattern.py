class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split()
        if len(pattern)!=len(words):
            return False
        chars= {}
        wor = {}
        
        for char, word in zip(pattern, words):
            if char in chars and chars[char] != word:
                return False
            if word in wor and wor[word] != char:
                return False
            chars[char] = word
            wor[word] = char
            
        return True
            