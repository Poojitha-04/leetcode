class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack=[]
        res=[0]*n
        prev_time=0
        splits=[log.split(':') for log in logs]
        for l, status, time in splits:
            fid = int(l)      
            time = int(time)
            if status == 'start':
                if stack:
                    res[stack[-1]] += time - prev_time
                stack.append(fid)
                prev_time = time
                
            elif status == 'end':
                res[stack.pop()] += time - prev_time + 1
                prev_time = time + 1
                
        return res