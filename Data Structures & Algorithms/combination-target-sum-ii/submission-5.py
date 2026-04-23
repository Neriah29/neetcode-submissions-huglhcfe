class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = set()

        def dfs(i, sub, tot):
            if tot == target:
                res.add(tuple(sub))
                return
            if i >= len(candidates) or tot > target:
                return

            sub.append(candidates[i])
            dfs(i+1, sub, tot + candidates[i])
            sub.pop()
            dfs(i+1, sub, tot)
        
        dfs(0, [], 0)
        return [list(tpl) for tpl in res]

            
            