class Solution:
    def smallestSubarrays(self, nums: list[int]) -> list[int]:
        n = len(nums)
        arr = [1] * n
        # Track the last seen index for each of the 30 bits
        last_seen_bit = [-1] * 30
        
        # Traverse backwards
        for j in range(n - 1, -1, -1):
            # Update the last seen position for each bit present in nums[j]
            for bit in range(30):
                if (nums[j] >> bit) & 1:
                    last_seen_bit[bit] = j
            
            # The furthest index needed to complete the max OR starting at j
            max_idx = j
            for bit in range(30):
                if last_seen_bit[bit] != -1:
                    max_idx = max(max_idx, last_seen_bit[bit])
            
            # Subarray length is the distance from j to that furthest index
            arr[j] = max_idx - j + 1
            
        return arr
