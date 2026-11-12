class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        best=0
        totalboth=min(costBoth, cost1 + cost2)*min(need1, need2)
        rem1=min(cost1,costBoth)*(need1-min(need1, need2))
        rem2=min(cost2,costBoth)*(need2-min(need1, need2))
        return totalboth+rem1+rem2