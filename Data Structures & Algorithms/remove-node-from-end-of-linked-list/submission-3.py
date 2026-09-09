# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        so we dont need to cover the case where n > lenght of the head

        A --> B --> C --> D --> None
        0,    1,   2,    3,   4, no more iterations
        """
        if not head.next:
            return None
        current_node = head
        count = 0
        while current_node:
            current_node = current_node.next
            count += 1
        
        nth_node = count - n
        current_node = head
        for i in range(nth_node-1):
            current_node = current_node.next

        current_node.next = current_node.next.next

        return head

