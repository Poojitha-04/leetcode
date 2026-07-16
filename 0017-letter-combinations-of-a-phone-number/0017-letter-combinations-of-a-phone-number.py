class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d={2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}
        if not digits:
            return []
        dp=[""]
        for digit in digits:
            c=d[int(digit)]
            nextdp=[]
            for comb in dp:
                for letter in c:
                    nextdp.append(comb+letter)
            dp=nextdp
        return dp

            
            

        