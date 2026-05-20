class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([i.lower() for i in s if i.isalnum() and i != ' '])
        if s == '':
            return True
        left = 0
        right = len(s) - 1

        while s[left] == s[right] and left < right:
            left += 1
            right -= 1
        return left >= right
