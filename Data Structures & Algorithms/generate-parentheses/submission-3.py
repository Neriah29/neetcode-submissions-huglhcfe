class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(cur, l, r):
            if l >= n and r >= n:
                res.append(cur)
                return
            
            if l < n:
                dfs(cur + "(", l + 1, r)

            if r < l:
                dfs(cur + ")", l, r + 1)
            
        dfs("(", 1, 0)
        return res

