class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        height=sorted(heights)
        count=0
        for i in range(len(heights)):
            if height[i]!=heights[i]:
                count+=1
        return count