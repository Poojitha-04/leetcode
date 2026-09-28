class Solution:
    def maxDepth(self, s: str) -> int:
        res=0
        Open,close=0,0
        for i in range(len(s)):
            if s[i]=='(':
                Open+=1
            elif s[i]==')':
                close+=1
                # res=max(res,Open-close)
            res = max(res, Open - close) 
        return res
