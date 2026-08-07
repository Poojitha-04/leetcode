class Solution:
    def maxProduct(self, n: int) -> int:
        strn=str(n)
        res=1
        if len(strn)<=2:
            return int(strn[0])*int(strn[1])
        s=sorted(strn,reverse=True)
        return int(s[0])*int(s[1])


        