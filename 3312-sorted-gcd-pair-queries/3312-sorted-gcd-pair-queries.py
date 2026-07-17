from collections import Counter
class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        if not nums:
            return []
        max_num = max(nums)
        counts = Counter(nums)
        gcd_counts = [0] * (max_num + 1)
        for g in range(max_num, 0, -1):
            total_multiples = sum(counts[c] for c in range(g, max_num + 1, g))
            total_pairs = (total_multiples * (total_multiples - 1)) // 2
            
            for multiple in range(2 * g, max_num + 1, g):
                total_pairs -= gcd_counts[multiple]
                
            gcd_counts[g] = total_pairs

        # 2. Build the prefix boundaries and a dense map of valid GCDs
        # This prevents the creation of a massive flattened array
        gcd_values = []
        prefix_sums = []
        current_total_pairs = 0
        
        for g in range(1, max_num + 1):
            if gcd_counts[g] > 0:
                current_total_pairs += gcd_counts[g]
                gcd_values.append(g)
                prefix_sums.append(current_total_pairs)
                
        # 3. Answer queries using binary search in O(log(M)) time
        s = []
        for q in queries:
            # bisect_right finds where index 'q' falls inside our prefix sum tiers
            idx = bisect.bisect_right(prefix_sums, q)
            s.append(gcd_values[idx])
            
        return s
