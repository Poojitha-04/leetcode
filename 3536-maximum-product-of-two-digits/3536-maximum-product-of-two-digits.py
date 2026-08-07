class Solution:
    def maxProduct(self, n: int) -> int:
    
        s=sorted(str(n),reverse=True)
        return int(s[0])*int(s[1])


        