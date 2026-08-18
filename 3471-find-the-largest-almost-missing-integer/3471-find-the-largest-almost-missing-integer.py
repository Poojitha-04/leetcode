class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        largest=-1
        n=len(nums)
        if k==n:
            return max(nums)
        if k==1:
            nums.sort(reverse=True)
            largest = next((x for x in nums if nums.count(x) == 1), -1)
            return largest
        else:
            
            first=nums.count(nums[0])
            last=nums.count(nums[-1])
            print(first,last)
            if first==last==1:
                return max(nums[0],nums[-1])
            if first>1 and last>1:
                return -1
            elif first>1:
                return nums[-1]
            elif last>1:
                return nums[0]
            

