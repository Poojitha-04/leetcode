class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        d={}
        for i in range(len(nums)):
            d[nums[i]]=d.get(nums[i],0)+1
        d = dict(sorted(d.items(), key=lambda item: item[1],reverse=True))
        return list(d)[0]

        