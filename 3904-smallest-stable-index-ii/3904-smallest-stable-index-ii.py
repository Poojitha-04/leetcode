class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        minnum=[nums[-1]]
        maxnum=[nums[0]]
        res=-1
        n=len(nums)
        for i in range(1,len(nums)):
            if nums[i]>maxnum[-1]:
                maxnum.append(nums[i])
            else:
                maxnum.append(maxnum[-1])
        for j in range(len(nums)-1,-1,-1):
            if nums[j]<minnum[-1]:
                minnum.append(nums[j])
            else:
                minnum.append(minnum[-1])
        
        for i  in range(len(maxnum)):
            # print(maxnum[i],minnum[i])
            if maxnum[i]-minnum[n-i]<=k:
                if res==-1 or i<res:
                    res=i
            # print(res)
        return res
                