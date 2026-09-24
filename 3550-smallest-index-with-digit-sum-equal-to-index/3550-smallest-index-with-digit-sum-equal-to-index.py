class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        res=0
        for i in range(len(nums)):
            temp=str(nums[i])
            sumnum=sum(int(i) for i in temp)
            if sumnum==i:
                return i
        return -1
        