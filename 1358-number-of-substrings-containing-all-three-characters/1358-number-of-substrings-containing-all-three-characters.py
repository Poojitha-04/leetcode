class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        seen={'a':-1,'b':-1,'c':-1}
        count=0
        for j,char in enumerate(s):
            if char in seen:
                seen[char]=j
            min_idx=min(seen['a'],seen['b'],seen['c'])
            if min_idx!=-1:   
                count+=min_idx+1
        return count
  
