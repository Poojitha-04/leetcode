class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # arr2=set(arr)
        arr1=sorted(set(arr))
        d={}
        for i in range(len(arr1)):
           d[ arr1[i]]=i
        res=[]
        for i in arr:
            # print(i,arr1.index(i)+1)
            res.append(d.get(i)+1)
        return res


        