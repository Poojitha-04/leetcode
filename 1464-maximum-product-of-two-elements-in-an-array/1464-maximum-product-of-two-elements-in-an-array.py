class Solution:
    def maxProduct(self, nums: List[int]) -> int:
       num1=max(nums)
       nums.remove(num1)
       num1-=1
       num2=max(nums)
       num2-=1
       return num1*num2