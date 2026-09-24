class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            sumnum=sum(int(i) for i in str(nums[i]))
            if sumnum==i:
                return i
        return -1
        