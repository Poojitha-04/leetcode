class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        res=0
        nums=[abs(x) for x in nums]
        nums.sort(reverse=True)
        n=len(nums)
        if n%2==0:
            n=n//2
        else:
            n=n//2+1
        for i in range(n) :
            res+=nums[i]**2
            # print(i,res)
        for i in range(n,len(nums)):
            res-=nums[i]**2
            # print(i,res)
        return res



        