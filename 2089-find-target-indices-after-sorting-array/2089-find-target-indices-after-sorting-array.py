class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        low, high = 0, len(nums) - 1
        res = []
        count = nums.count(target)
        if count == 0:
            return res
            
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                res.append(mid)
                
                # Expand Right completely
                r = mid + 1
                while r < len(nums) and nums[r] == target:
                    res.append(r)
                    r += 1
                    
                # Expand Left completely (Fix: using >= 0 to include index 0)
                l = mid - 1
                while l >= 0 and nums[l] == target:
                    res.append(l)
                    l -= 1
                
                # Once we find the target group and expand, we have all of them!
                return sorted(res)
                    
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
                
        return sorted(res)
