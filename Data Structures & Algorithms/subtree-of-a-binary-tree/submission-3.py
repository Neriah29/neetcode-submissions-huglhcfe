# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
            
        if not root: return False

        if self.isSametree(root, subRoot):
            return True
        
        return (self.isSubtree(root.right, subRoot) or
                self.isSubtree(root.left, subRoot))
        return False
  

    def isSametree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val == q.val:
            return (self.isSametree(p.left, q.left) and 
                    self.isSametree(p.right, q.right))
        return False