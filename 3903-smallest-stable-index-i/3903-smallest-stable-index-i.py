class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        res=101
        for i in range(len(nums)):
            n= max(nums[0:i+1])-min(nums[i:])
            print(n)
            if n<=k and i<res:
                res=i
    
        return res if res<101 else -1
            

        