class Solution:
    def minimumPushes(self, word: str) -> int:
        if len(word)<=8:
            return len(word)
        elif len(word)>8 and len(word)<=16:
            return 8+((len(word)-8)*2)
        elif len(word)>16 and len(word)<=24:
            return 24+((len(word)-16)*3)
        else:
            return 24+8*3+((len(word)-24)*4)
            