class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r  = 0, len(nums)-1
        while l <= r:
            m = (l+r)//2

            if nums[r] < nums[m]:
                l = m + 1
            elif nums[l] < nums[m]:
                r = m - 1
            else:
                return nums[m]


