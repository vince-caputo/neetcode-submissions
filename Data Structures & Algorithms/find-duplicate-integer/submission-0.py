class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        st = set()
        while nums:
            x = nums.pop()
            if x in st:
                return x
            st.add(x)