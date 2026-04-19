class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) -1
        while l <= r:
            curr = nums[l] + nums[r]
            if curr > target:
                r -= 1
            elif curr < target:
                l += 1
            else:
                return [l, r]