# from fractions import Fraction
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        l=[]
        for i in range(1,n):
            for j in range(i+1,n+1):
                # print(i,j)
                if math.gcd(i,j)==1:
                    l.append(f"{i}/{j}")
            
        return l 
        