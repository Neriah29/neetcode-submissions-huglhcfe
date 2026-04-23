class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, sub, tot):
            if tot == target:
                res.append(sub.copy())
                return
            if i >= len(candidates) or tot > target:
                return

            sub.append(candidates[i])
            dfs(i+1, sub, tot + candidates[i])
            sub.pop()
            if i + 1< len(candidates) and candidates[i+1] != candidates[i]:
                dfs(i+1, sub, tot)
        
        dfs(0, [], 0)
        return res

            
            