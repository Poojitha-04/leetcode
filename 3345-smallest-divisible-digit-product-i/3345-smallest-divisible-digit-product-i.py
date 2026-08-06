class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        temp=str(n)
        temp1=int(temp[0])
        if int(temp[-1])==0:
            return n
        if t>n:
            n=t
        num=n+10
        for i in range(n,num):
            if i>=10:
                if (temp1*(i%10))%t==0:
                    return i
            else:
                if (i%t)==0:
                    return i

        
        