class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # res=0
        # nums=[abs(x) for x in nums]
        # nums.sort(reverse=True)
        # n=len(nums)
        # if n%2==0:
        #     n=n//2
        # else:
        #     n=n//2+1
        # for i in range(n) :
        #     res+=nums[i]**2
        #     # print(i,res)
        # for i in range(n,len(nums)):
        #     res-=nums[i]**2
        #     # print(i,res)
        # return res
        num=[x**2 for x in nums]
        num.sort(reverse=True)
        res=0
        n=len(nums)
        if n%2==0:
            n=n//2
        else:
            n=n//2+1
        res+=sum(x for x in num[0:n])
        # print(res)
        res-=sum(x for x in num[n:len(nums)])
        return res





        