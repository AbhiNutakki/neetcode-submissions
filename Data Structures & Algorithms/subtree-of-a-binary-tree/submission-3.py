# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot == None:
            return True

        if root == None:
            return False
        
        if self.isSameTree(root,subRoot):
            return True
        
        return (
            self.isSubtree(root.left,subRoot)
            or self.isSubtree(root.right,subRoot)
        )


    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        
        if root is None or subRoot is None:
            return False
        
        if root.val != subRoot.val:
            return False
        

        leftTree = self.isSameTree(root.left,subRoot.left)
        rightTree = self.isSameTree(root.right,subRoot.right)

        if leftTree and rightTree:
            return True
        else:
            return False
        