class Solution:
    def minimumMoney(self, transactions: list[list[int]]) -> int:
        res = v = 0
        for i,j in transactions:
            res += max(0, i - j)
            v = max(v, min(i, j))
        return res + v
        