class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n==0:
            return 0
        num=''
        n1=str(n)
        s=0
        for i in range(len(n1)):
            if n1[i]=='0':
                continue
            else:
                num+=n1[i]
                s+=int(n1[i])
        return int(num)*s