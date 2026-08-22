class Solution:
    def checkDivisibility(self, n: int) -> bool:
        strn=str(n)
        total=0
        prod=1
        for i in strn:
            total+=int(i)
            prod*=int(i)
        if n%(total+prod)==0:
            return True
        return False

        