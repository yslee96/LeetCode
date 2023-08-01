# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(cur_node, pre_sum, is_root):
            ret = 0
           # print(cur_node.val, pre_sum, is_root)
            if cur_node.val + pre_sum == targetSum:
                ret+=1
            
            if cur_node.left:
                ret += dfs(cur_node.left, pre_sum + cur_node.val, False)
                if is_root:
                    ret += dfs(cur_node.left, 0, True)

            if cur_node.right:
                ret += dfs(cur_node.right, pre_sum + cur_node.val, False)
                if is_root:
                    ret += dfs(cur_node.right, 0, True)
            
            return ret
        
        return dfs(root, 0, True) if root else 0