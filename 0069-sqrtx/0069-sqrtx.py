class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        y = x
        z = (y + (x/y)) // 2
        while abs(y - z) >= 0.00001:
            y = z
            z = (y + (x/y)) / 2
        
        return int(z)

        