class Solution:
    def minMoves(self, nums: list[int]) -> int:
        minnum=min(nums)
        return sum(num - minnum for num in nums)
