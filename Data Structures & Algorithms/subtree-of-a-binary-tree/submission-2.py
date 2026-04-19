# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        return (self.isSametree(root, subRoot) or 
                self.isSametree(root.right, subRoot) or 
                self.isSametree(root.left, subRoot)) 

  

    def isSametree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val == q.val:
            return (self.isSametree(p.left, q.left) and 
                    self.isSametree(p.right, q.right))
        return False