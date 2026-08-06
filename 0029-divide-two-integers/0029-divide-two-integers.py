class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
    # 1. Handle 32-bit signed integer overflow edge case
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # 2. Determine the sign of the result
        # If one is negative and the other is positive, sign is negative
        negative = (dividend < 0) ^ (divisor < 0)

        # 3. Work with absolute values
        amt_dividend = abs(dividend)
        amt_divisor = abs(divisor)
        quotient = 0

        # 4. Perform bitwise division
        while amt_dividend >= amt_divisor:
            temp_divisor = amt_divisor
            count = 0
            
            # Double the divisor using left shift until it exceeds dividend
            while amt_dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                count += 1
                
            # Subtract the largest shifted multiple from dividend
            amt_dividend -= temp_divisor
            # Add the power of 2 to the quotient
            quotient += (1 << count)

        # 5. Apply sign and return
        return -quotient if negative else quotient
