class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        subset = []
        candidates.sort()

        def dfs (i, cur, total):
            if total == target:
                res.add(tuple(subset))
                return
            if total > target or i >= len(candidates) :
                return


            subset.append(candidates[i])
            dfs(i+1, cur, total + candidates[i])

            subset.pop()
            dfs(i+1, cur, total )


        dfs(0, subset, 0)
        return [list(t) for t in res]
