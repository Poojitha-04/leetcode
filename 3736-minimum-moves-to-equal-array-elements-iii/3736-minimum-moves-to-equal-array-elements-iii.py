class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxnum=max(nums)
        return sum(maxnum-num for num in nums)
        