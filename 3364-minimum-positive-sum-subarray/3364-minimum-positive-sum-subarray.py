import math
from typing import List


class Solution:

  def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        res = math.inf
        n = len(nums)

        for i in range(n):
            curr_sum = 0
            for j in range(i, min(n, i + r)):
                curr_sum += nums[j]
                length = j - i + 1
                if length >= l and curr_sum > 0:
                    res = min(res, curr_sum)

        return -1 if res == math.inf else res
