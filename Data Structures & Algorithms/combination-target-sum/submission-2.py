class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        tring to do a dfs where for the one on the left the curr[i] is appended
        """
        res = []
        subset = []

        def dfs(i, subset):
            cur = sum(subset)
            if cur == target:
                res.append(subset.copy())
                return
            if sum(subset) > target or i >= len(nums):
                return 

            subset.append(nums[i])
            dfs(i, subset)
            subset.pop()
            dfs(i + 1, subset)
        
        dfs(0, subset)
        return res