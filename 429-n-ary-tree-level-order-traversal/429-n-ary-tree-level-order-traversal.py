"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        def dfs(root, level):
            if root == None: return
            if level == len(levels):
                levels.append([])
            levels[level].append(root.val)
            for child in root.children:
                dfs(child, level+1)
        levels = []
        dfs(root, 0)
        return levels