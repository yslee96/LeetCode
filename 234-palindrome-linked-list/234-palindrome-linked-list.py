# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node_data = []
        while(head):
            node_data.append(head.val)
            head = head.next
        return node_data == node_data[::-1]