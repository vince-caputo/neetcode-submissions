class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == 0 and target == 0:
                return 2
            return int(nums[0] == target or -nums[0] == target)

        return self.findTargetSumWays(nums[1:], target - nums[0]) + self.findTargetSumWays(nums[1:], target + nums[0])