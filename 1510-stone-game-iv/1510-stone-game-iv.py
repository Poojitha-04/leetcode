class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            k = 1
            # Test every perfect square less than or equal to the current pile size i
            while k * k <= i:
                # If subtracting k*k forces the opponent into a losing position, 
                # then the current player wins!
                if not dp[i - k * k]:
                    dp[i] = True
                    break  # No need to check other moves; we found a winning strategy
                k += 1
                
        return dp[n]
        

            