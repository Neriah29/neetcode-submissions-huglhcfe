class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(ar):
            if not ar:
                return [[]]
            res = []
            perm = dfs(ar[1:])
            for p in perm:
                print(p)
                for i in range(len(p) + 1):
                    cur = p.copy()
                    cur.insert(i, ar[0])
                    res.append(cur)
            
            return res

        return (dfs(nums))
