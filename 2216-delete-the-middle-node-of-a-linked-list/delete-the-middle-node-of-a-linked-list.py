# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode (next = head)
        p1=p2=temp
        while p2.next is not None and p2.next.next is not None:
            p1 = p1.next
            p2 = p2.next.next
        p1.next = p1.next.next
        return temp.next