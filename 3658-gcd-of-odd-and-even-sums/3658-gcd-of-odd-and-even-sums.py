class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd=0
        even=0
        for i in range(2*n):
            if i%2==0:
                even+=i
            else:
                odd+=i
        return math.gcd(odd,even)

        