class Solution:
    def minimumPushes(self, word: str) -> int:
        d={}
        for i in range(len(word)):
            d[word[i]]=d.get(word[i],0)+1
        d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        res=0
        keys=list(d.keys())
        # print(keys,len(keys))
        if len(d)<=8:
            for i in d.keys():
                res+=d.get(i)
        elif len(d)>8 and len(d)<=16:
            for i in range(len(d)):
                if i<=7:
                    res+=d.get(keys[i])
                else:
                    print(res,d.get(keys[i]))
                    res+=(d.get(keys[i])*2)
        elif len(d)>16 and len(d)<=24:
            for i in range(len(d)):
                if i<=7:
                    res+=d.get(keys[i])
                elif i>7 and i<=15:
                    res+=d.get(keys[i])*2
                else:
                    res+=d.get(keys[i])*3
        else:
            for i in range(len(d)):
                if i<=7:
                    res+=d.get(keys[i])
                elif i>7 and i<=15:
                    res+=d.get(keys[i])*2
                elif i>15 and i<=23:
                    res+=d.get(keys[i])*3
                else:
                    res+=d.get(keys[i])*4
        return res
                
