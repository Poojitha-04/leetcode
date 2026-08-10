class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i,j=0,len(needle)
        while j<=len(haystack):

            if haystack[i:j]==needle:
                return i

            else:
                i+=1
                j=i+len(needle)
        return -1


        
        
        