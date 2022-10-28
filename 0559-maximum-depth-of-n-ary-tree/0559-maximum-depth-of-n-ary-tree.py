"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(root, depth):
            if not root: return depth
            ret = depth
            for child in root.children:
                ret = max(ret, dfs(child, depth+1))
            return ret
        return 0 if not root else dfs(root, 1)