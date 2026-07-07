class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n==0:
            return 0
        num1=''
        n1=str(n)
        s=0
        for i in range(len(n1)):
            if n1[i]=='0':
                continue
            else:
                num1+=n1[i]
                s+=int(n1[i])
        num= int(num1)
        return int(num1)*s