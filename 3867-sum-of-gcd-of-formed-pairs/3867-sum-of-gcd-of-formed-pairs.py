class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        res=[]
        maxi=nums[0]
        for i in range(len(nums)):
            if maxi<nums[i]:
                maxi=nums[i]
            res.append(math.gcd(maxi,nums[i]))
        res.sort()
        s=[]
        while len(res)>1:
            s.append(math.gcd(res.pop(),res.pop(0)))
        return sum(s)


        