import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output =[]
        for num_idx in range(nums):
            num = math.prod(nums)/nums[num_idx]
            output.append(num)
        return output