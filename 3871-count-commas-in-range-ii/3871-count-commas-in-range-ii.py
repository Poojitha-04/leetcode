class Solution:
    def countCommas(self, n: int) -> int:
        if n <= 999:
            return 0
        if n >= 1000 and n < 1000000:
            return n - 999
        if n >= 1000000 and n < 1000000000:
            num2 = (n - 999999) * 2
            return 999000 + num2
        if n >= 1000000000 and n < 1000000000000:
            num2 = (n - 999999999)
            return (num2 * 3) + 1998999000
        if n >= 1000000000000 and n < 1000000000000000:
            num2 = (n - 999999999999)
            return num2 * 4 + 2998998999000
        if n < 1000000000000000000:
            num2 = n - 999999999999999
            return num2 * 5 + 3998998998999000

            



