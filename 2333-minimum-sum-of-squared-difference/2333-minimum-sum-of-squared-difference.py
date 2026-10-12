class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        # Step 1: Calculate initial absolute differences
        diffs = [abs(n1 - n2) for n1, n2 in zip(nums1, nums2)]
        max_diff = max(diffs)
        
        # Step 2: Create a frequency bucket for the differences
        bucket = [0] * (max_diff + 1)
        for d in diffs:
            bucket[d] += 1
            
        # Total operations available
        k = k1 + k2
        
        # Step 3: Process from the largest difference down to 1
        for d in range(max_diff, 0, -1):
            if bucket[d] == 0:
                continue
                
            # If we have enough k to reduce all elements of size 'd' to 'd-1'
            if k >= bucket[d]:
                k -= bucket[d]
                bucket[d - 1] += bucket[d]
                bucket[d] = 0
            else:
                # Reduce as many as we can with the remaining k
                bucket[d - 1] += k
                bucket[d] -= k
                k = 0
                break
                
        # Step 4: Calculate the final sum of squares
        ans = 0
        for d in range(1, max_diff + 1):
            if bucket[d] > 0:
                ans += bucket[d] * (d ** 2)
                
        return ans
