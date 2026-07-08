class Solution:
    def reverse(self, x: int) -> int:
        high,low=(2**31)-1,-2**31
        # print(high)
        sign=1
        if x<0:
            sign=-1
        x=abs(x)
        n=str(x)
        rev=n[::-1]
        rev=sign*int(rev)
        if rev>high or rev<low:
            return 0
        return rev

        


            