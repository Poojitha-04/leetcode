class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        res=math.inf
        for i in range(len(nums)):
            n= max(nums[0:i+1])-min(nums[i:])
            # print(n)
            if n<=k and i<res:
                res=i
        if res!=math.inf:
            return res
        return -1
            

        