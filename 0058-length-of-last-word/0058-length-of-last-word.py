class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length=0
        s=s.strip()
        # print(s)
        for i in range(len(s)-1,-1,-1):
            
            # print(s[i])
            if s[i]==" ":
                break
            else:
                length+=1
        return length
        
        