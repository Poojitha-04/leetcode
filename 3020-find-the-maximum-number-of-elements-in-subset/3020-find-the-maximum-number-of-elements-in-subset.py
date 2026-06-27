class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count=Counter(nums)
        ones=count.get(1,0)
        ans=ones if ones%2 else ones-1
        count.pop(1,None)
        for i in nums:
            res=0
            x=i
            while x in count and count[x]>1:
                res+=2
                x*=x
            ans=max(ans,res+(1 if x in count else -1))
        return ans