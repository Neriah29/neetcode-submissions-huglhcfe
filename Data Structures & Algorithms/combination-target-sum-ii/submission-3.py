class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(start, cur, total):
            # Base Case: Found a valid combination
            if total == target:
                res.append(list(cur))
                return
            
            # Explore choices for the "current slot"
            for i in range(start, len(candidates)):
                # 2. PRUNING: Since it's sorted, if this number is too big, 
                # every number after it will also be too big.
                if total + candidates[i] > target:
                    break
                
                # 3. SKIP DUPLICATES: Only use the first occurrence of a number 
                # for this specific position in the combination.
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                # Standard Backtracking
                cur.append(candidates[i])
                dfs(i + 1, cur, total + candidates[i])
                cur.pop()
        
        dfs(0, [], 0)
        return res