class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(s, l, r):
            if l >= n and r >= n:
                res.append(s)
                return
            
            if l < n:
                dfs(s+"(", l+1, r)
            
            if r < l:
                dfs(s+")", l, r+1)
            
        dfs("(", 1, 0)
        return res


        