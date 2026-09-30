class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        stack=[]
        s=0
        for i in seq:
            if i=='(':
                s+=1
                stack.append(s%2)
            if i==')':
                stack.append(s%2)
                s-=1
        return stack
        