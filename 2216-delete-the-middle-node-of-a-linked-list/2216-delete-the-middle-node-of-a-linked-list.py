# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = 1
        tmp = head
        while tmp.next:
            cnt+=1
            tmp = tmp.next

        middle_idx = math.floor(cnt/2)
        if middle_idx == 0:
            head = head.next
            return head
        cur = pre = head
        while middle_idx:
            pre = cur
            cur = cur.next
            middle_idx -=1
        pre.next = cur.next
        return head