import collections
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        d=collections.defaultdict(list)
        for i in range(len(nums)):
             d[nums[i]].append(i)
        for key ,val in d.items():
            if len(val)>1:
                for i in range(1, len(val)):
                    diff = abs(val[i] - val[i - 1])
                    if diff<=k:
                        return True
        return False


        