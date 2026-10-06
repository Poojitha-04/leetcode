class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res=[]
        for i in range(len(s)) :
            if s[i]=='(':
                res.append(s[i])
            elif res and s[i]==')' and res[-1]=='(':
                   res.pop()
            else:
                res.append(s[i])
        return len(res)
        