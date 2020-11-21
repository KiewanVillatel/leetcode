"""
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Note:

    Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For this problem, assume that your function returns 231 − 1 when the division result overflows.



Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.

Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.

Example 3:

Input: dividend = 0, divisor = 1
Output: 0

Example 4:

Input: dividend = 1, divisor = 1
Output: 1



Constraints:

    -231 <= dividend, divisor <= 231 - 1
    divisor != 0
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        # compute sign of the quotient
        sign = 1 if (divisor > 0 and dividend > 0) or (divisor < 0 and dividend < 0) else -1

        # work with positive divisor and dividend
        if divisor < 0:
            divisor = -divisor
        if dividend < 0:
            dividend = -dividend

        # Build quotient using a base-2 decomposition of the quotient
        # eg. dividend = 10, divisor = 3
        # 10 = 6   + 3
        #    = 3*2 + 3*1
        # quotient = 2 + 1
        #          = 3
        power_divisor = divisor
        power_divisors = {1: power_divisor}

        power = 1
        while power_divisor < dividend:
            power = power + power
            power_divisor = power_divisor + power_divisor
            power_divisors[power] = power_divisor

        quotient = 0
        divisor = 0
        for power in sorted(power_divisors.keys(), reverse=True):
            tmp = divisor + power_divisors[power]
            if tmp <= dividend:
                divisor += power_divisors[power]
                quotient += power

            # Check for overflow
            if (sign == 1 and quotient > (pow(2, 31) - 1)) or (sign == -1 and quotient > pow(2, 31)):
                return pow(2, 31) - 1

        # Check for signed quotient
        return quotient if sign == 1 else -quotient

assert (Solution().divide(10, 3) == 3)
assert (Solution().divide(7, -3) == -2)
assert (Solution().divide(0, 1) == 0)
assert (Solution().divide(1, 1) == 1)
assert (Solution().divide(pow(2, 31), 1) == pow(2, 31)-1)
assert (Solution().divide(-pow(2, 31), -1) == pow(2, 31)-1)
assert (Solution().divide(-pow(2, 31), -pow(2, 31)) == 1)
assert (Solution().divide(-pow(2, 31), 1) == -pow(2, 31))
