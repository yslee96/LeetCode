# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        tmp1 = head
        nodeCnt = 1
        while(tmp1.next):
            nodeCnt+=1
            tmp1 = tmp1.next
        if nodeCnt%2==0:
            half = nodeCnt//2
            front = []
            tmp2 = head
            for _ in range(half):
                front.append(tmp2.val)
                tmp2 = tmp2.next
            front.reverse()
            print(front)
            for i in range(half):
                if tmp2.val != front[i]:
                    return False
                tmp2 = tmp2.next
            return True
        else:
            mid = (nodeCnt+1)//2
            front = []
            tmp3 = head
            for _ in range(mid-1):
                front.append(tmp3.val)
                tmp3 = tmp3.next
            front.reverse()
            print(front)
            for i in range(mid-1):
                tmp3 = tmp3.next
                if tmp3.val != front[i]:
                    return False
            return True
        