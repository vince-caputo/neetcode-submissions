class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits == [9] * len(digits):
            return [1] + ([0] * len(digits))
        
        carrying = True
        i = -1
        while carrying:
            if digits[i] == 9:
                digits[i] -= 9
                i -= 1
            else:
                digits[i] += 1
                carrying = False
        
        return digits