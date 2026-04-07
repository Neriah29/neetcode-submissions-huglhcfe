# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        def height(node):
            if not node:
                return 0
            
            l = 1 + height(node.left)
            r = 1 + height(node.right)
            return max(l, r)

        m = 0
        diam =   height(root.left) + height(root.right)
        m = max(m, diam)
        return m