import statistics
class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        med=statistics.median(nums)
        res=sum(abs(med-num) for num in nums)
        return int(res)
        