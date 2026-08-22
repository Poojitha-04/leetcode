class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
       perfect=[6,28,496,8128,33550336,8589869056]
       if  num in perfect:
            return True
       return False
    


        