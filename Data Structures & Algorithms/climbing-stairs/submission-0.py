class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        small = 1
        big = 2
        nxt = 0
        
        while n > 2:
            nxt = big + small
            small = big
            big = nxt
            n -= 1

        return nxt