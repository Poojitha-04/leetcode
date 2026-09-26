class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        res=''
        i=0
        d={}
        for j in range(len(knowledge)):
            d[knowledge[j][0]]=knowledge[j][1]
        # print(d)
        while i <len(s):
            print(s[i])
            if s[i]=='(' :
                i+=1
                temp=''
                while s[i]!=')':
                    temp+=s[i]
                    # print(temp)
                    i+=1
                # print(temp)
                if temp in d.keys():
                    res+=d.get(temp)
                else:
                    res+='?'
                i+=1
            else:
                res+=s[i]
                i+=1
        return res
            

        