# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def dfs(node: TreeNode, depth):
            ret = depth
            if node and node.left:
                ret = max(ret, dfs(node.left, depth+1))
            if node and node.right:
                ret = max(ret,dfs(node.right, depth+1))

            return ret
        ans = dfs(root, 1)
        return ans