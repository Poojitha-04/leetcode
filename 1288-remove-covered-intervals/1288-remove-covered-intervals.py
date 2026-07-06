class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: (x[0],-x[1]))
        count = 0
        maxend=0
        for _, end in intervals:
            if end > maxend:
                count += 1
                maxend = end 
                
        return count


                    

                