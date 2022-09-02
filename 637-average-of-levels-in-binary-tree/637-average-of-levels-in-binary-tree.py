# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
            result = []
            current_level = [root]
            while current_level:
                level_sum = 0
                next_level = []
                for node in current_level:
                    level_sum += node.val
                    if node.left: next_level.append(node.left)
                    if node.right: next_level.append(node.right)
                result.append(level_sum / len(current_level))
                current_level = next_level
            return result