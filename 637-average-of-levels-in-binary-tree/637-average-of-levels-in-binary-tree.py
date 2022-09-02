# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        def traverse(node, depth):
            numsByDepths[depth].append(node.val)
            if node.left:
                traverse(node.left, depth+1)
            if node.right:
                traverse(node.right, depth+1)
                
        numsByDepths = [ [] for _ in range(10001)]
        traverse(root, 0)
        answers = []
        for i in range(10001):
            if len(numsByDepths[i])==0:
                break
            else:
                answers.append(sum(numsByDepths[i]) / len(numsByDepths[i]))
                
        return answers