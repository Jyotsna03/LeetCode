# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
# 2 pointer to iterate 
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
# reverse the LL
        prev = None
        while slow:
            curr = slow.next
            slow.next = prev
            prev = slow
            slow = curr
# palindrome check 
        left, right = head, prev
        while right:
            if left.val != right.val: 
                return False
            left = left.next
            right = right.next
        return True                               




        