# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        st = set()
        curr = head
        while curr is not None:
            if curr in st:
                return True
            st.add(curr)
            curr = curr.next
        return False        
        