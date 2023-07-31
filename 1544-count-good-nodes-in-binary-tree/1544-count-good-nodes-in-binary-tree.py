# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def find_goods(cur_node, pre_max):
            ret = 0
            if cur_node.val >= pre_max:
                ret +=1
            
            cur_max = max(cur_node.val, pre_max)

            if cur_node.left:
                ret += find_goods(cur_node.left, cur_max)
            if cur_node.right:
                ret += find_goods(cur_node.right, cur_max)
            
            return ret

        return find_goods(root, root.val)
