class Solution:
    def minimumPushes(self, word: str) -> int:
        d={}
        for i in range(len(word)):
            d[word[i]]=d.get(word[i],0)+1
        print(d,len(word))
        if len(word)<=8:
            return len(word)
        elif len(word)>8 and len(word)<=16:
            return 8+((len(word)-8)*2)
        elif len(word)>16 and len(word)<=24:
            return 24+((len(word)-16)*3)
        else:
            return 24+8*3+((len(word)-24)*4)
            