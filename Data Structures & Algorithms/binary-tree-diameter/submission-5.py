# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiam = 0

        def height(node):
            nonlocal maxDiam
            if not node:
                return 0

            leftHeight, rightHeight = height(node.left), height(node.right)
            currHeight = max(leftHeight, rightHeight) + 1
            maxDiam = max(maxDiam, (leftHeight + rightHeight))
            print()
            return currHeight
        height(root)
        return maxDiam
            
