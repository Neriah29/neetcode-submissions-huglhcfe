# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
       we are going to build this recursviely 
        hmm, so we have the base case of none,
        then recursive case is, using ranges.
        """
        if not preorder:
            return None
        
        #create the tree node
        root = TreeNode(preorder[0])
        currIndex = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:currIndex+1], inorder[:currIndex])
        root.right = self.buildTree(preorder[currIndex+1:], inorder[currIndex + 1:])

        return root