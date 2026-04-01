# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Thought process:
        return where they first split in the traversal
        we are told that both p and q will exist so no need to do further checks

        scenarios:
        both are greater than or less than. in that case, recursion on that side
        one is less and the other is greater, in that case, return root
        one/both are equal to the root, in that case return root
        """
        #check if both higher
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        #check if both lower
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        #check if one/both are equal to
        if p.val == root.val or q.val == root.val:
            return root
        
        return root
        

