# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #base case is when length == 1 or 0
        if not head or not head.next:
            return head
        
        newlist = self.reverseList(head.next)

        head.next.next = head
        head.next = None
        
        return newlist