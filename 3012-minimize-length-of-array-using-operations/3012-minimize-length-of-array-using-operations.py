class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        minele=min(nums)
        for num in nums:
            if num%minele:
                return 1
        return (nums.count(minele)+1)//2