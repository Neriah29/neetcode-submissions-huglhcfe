class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, sub, tot, flag):
            
            if tot == target:
                res.append(sub.copy())
                return
            if i >= len(candidates) or tot > target:
                return



            sub.append(candidates[i])
            if not flag:
                dfs(i+1, sub, tot + candidates[i], False)
                sub.pop()
            else:
                if i + 1< len(candidates) and candidates[i+1] == candidates[i]:
                    flag = True
                sub.pop()
                dfs(i+1, sub, tot, False )

            if i + 1< len(candidates) and candidates[i+1] == candidates[i]:
                flag = True
            dfs(i+1, sub, tot, flag)
        
        dfs(0, [], 0, False)
        return res

            
            