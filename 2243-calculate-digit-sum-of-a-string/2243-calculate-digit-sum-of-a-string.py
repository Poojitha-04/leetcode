class Solution:
    def digitSum(self, s: str, k: int) -> str:
        # res=0
        while len(s)>k:
            s=self.sumfunc(s,k)
        return str(s)
    def sumfunc(self,s,k)->str:
        new_s = []
        for i in range(0, len(s), k):
            total = sum(int(digit) for digit in s[i:i+k])
            new_s.append(str(total))
        return "".join(new_s)
    
        