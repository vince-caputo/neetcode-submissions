class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_prior(nums):
            n = len(nums)

            if n <= 2:
                return max(nums)
            
            if n == 3:
                return max(nums[1], nums[0] + nums[2])

            nums[2] += nums[0]

            for i in range(3, n):
                nums[i] += max(nums[i - 3], nums[i - 2])

            return max(nums[-1:-3:-1])

        n = len(nums)
        if len(nums) <= 3:
            return max(nums)

        if len(nums) == 4:
            return max(nums[0] + nums[2], nums[1] + nums[3])

        if len(nums) == 5:
            return max(nums[0] + max(nums[2], nums[3]), nums[1] + max(nums[3], nums[4]), nums[2] + nums[4])

        
        

        return max(nums[0] + rob_prior(nums[2: n - 1]), nums[1] + rob_prior(nums[3:]), nums[-1] + nums[2] + rob_prior(nums[4: n - 2]))

        