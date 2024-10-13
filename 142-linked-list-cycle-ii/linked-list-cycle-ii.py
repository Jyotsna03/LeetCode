# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # Initialize two pointers
        slow, fast = head, head
        
        # Detect if a cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # Cycle detected
            if slow == fast:
                # Find the start of the cycle
                pointer = head
                while pointer != slow:
                    pointer = pointer.next
                    slow = slow.next
                
                return pointer  # Start of the cycle
        
        return None 
        