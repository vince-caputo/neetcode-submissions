class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while True:
            visited.add(n)
            curr = 0
            while n > 0:
                curr += (n % 10) ** 2
                n //= 10
            if curr == 1:
                return True
            elif curr in visited:
                return False
            n = curr
                