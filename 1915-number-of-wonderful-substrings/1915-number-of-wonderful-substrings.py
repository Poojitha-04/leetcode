class Solution:
    # def iswonderful(self,word)->int:
    #     count=Counter(word)
    #     res=0
    #     for cnt in count.values():
    #         if cnt%2==1:
    #             res+=1
    #     if res>1:
    #         return 0
    #     return 1


    def wonderfulSubstrings(self, word: str) -> int:
        count=0
        d={0:1}
        m=0
        for i in range(len(word)):
           s=ord(word[i])-ord('a')
           m^=(1<<s)
           count+=d.get(m,0)
           for j in range(10):
                odd_variant = m ^ (1 << j)
                count += d.get(odd_variant, 0)
           d[m] = d.get(m, 0) + 1
            
        return count


            