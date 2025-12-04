class Solution:
    def reverse(self, x: int) -> int:
        # Define 32-bit signed integer limits
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        sign = 1
        if x < 0:
            sign = -1
            x = -x

        # Reverse the digits
        reversed_x = int(str(x)[::-1])
        
        # Apply sign
        reversed_x *= sign

        # Check for overflow
        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0
        
        return reversed_x
