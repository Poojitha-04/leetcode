class Solution:
    def stoneGameII(self,piles: list[int]) -> int:
        n = len(piles)
        
        # 1. Create suffix sums
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        memo = {}
        
        # 2. Define the recursive DP function
        def dp(i, m):
            # Base case: if we can take all remaining piles, take them
            if i + 2 * m >= n:
                return suffix_sum[i]
            
            if (i, m) in memo:
                return memo[(i, m)]
            
            # Maximize stones by minimizing opponent's yield
            max_stones = 0
            for x in range(1, 2 * m + 1):
                opponent_stones = dp(i + x, max(m, x))
                current_stones = suffix_sum[i] - opponent_stones
                max_stones = max(max_stones, current_stones)
                
            memo[(i, m)] = max_stones
            return max_stones

        # The game starts at index 0 with M = 1
        return dp(0, 1)

                


            