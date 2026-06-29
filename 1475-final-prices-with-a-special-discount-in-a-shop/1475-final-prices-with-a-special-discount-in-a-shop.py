class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res=[]
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                # print(i,j)
                if prices[i]>=prices[j]:
                    res.append(prices[i]-prices[j])
                    break
            else:
                res.append(prices[i])
        return res
    

        