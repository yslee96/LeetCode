# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def buildTree(nums, left, right):
            if left <= right:
                mid = left + (right-left)//2
                node = TreeNode(nums[mid])
                node.left = buildTree(nums, left, mid-1)
                node.right =buildTree(nums, mid+1, right)
                return node 
        return buildTree(nums, 0, len(nums)-1)