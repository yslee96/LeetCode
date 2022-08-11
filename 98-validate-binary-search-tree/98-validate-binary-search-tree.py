# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(curNode, lower, upper):
            if not self.valid:
                return
            if curNode.left:
                if curNode.val > curNode.left.val and curNode.left.val > lower:
                    traverse(curNode.left, lower, curNode.val)
                else:
                    self.valid = False
            if curNode.right:
                if curNode.val < curNode.right.val and curNode.right.val < upper:
                    traverse(curNode.right, curNode.val, upper)
                else:
                    self.valid = False
                    
        self.valid = True
        traverse(root, -float('inf'), float('inf'))
        return self.valid