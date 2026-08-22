class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res=[]
        for i in range(left,right+1):
            stri=str(i)
            for j in stri:
                if int(j)==0:
                    break
                if i%(int(j))!=0:
                   break
            else:
                res.append(i)
        return res
                

