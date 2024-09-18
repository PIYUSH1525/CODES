# Given; a; signed; 32 - bit; integer; x,return x with its digits reversed.If reversing x causes the value to go outside the signed 32-bit integer range[-231, 231 - 1], then return 0.Assume; the; environment; does; not allow; you; to; store; 64 - bit; integers(signed or unsigned).; Example; 1: Input: x = 123; Output: 321

class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if x <0:
            sign = -1
        else:
            sign = 1
        x = abs(x)
        ans = 0
        while x != 0:
            rem = x % 10
            ans = ans * 10 + rem
            x = x//10
            ans = sign* ans
        if ans < INT_MIN or ans > INT_MAX:
            return 0
        return ans





