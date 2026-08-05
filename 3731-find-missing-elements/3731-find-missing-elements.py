class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        minel=min(nums)
        maxele=max(nums)
        res=[]
        for i in range(minel,maxele):
            if i in nums:
                continue
            else:
                res.append(i)
        return res
