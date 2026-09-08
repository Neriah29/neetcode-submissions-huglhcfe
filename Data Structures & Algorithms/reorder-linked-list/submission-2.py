# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        i am thinking that we send a right pointer down to the far right 
        and then have some kind of recursive modifications 
        involving having
        """

        left = right = head
        prev_map= {}

        while right.next: #right is Never None, always a node
            prev = right
            right = right.next
            prev_map[right] = prev
        

        #how will we keep track of the previous?
        def rearrange(left_node, right_node, prev_map):
            #base case:
            if left_node == right_node or left_node.next == right_node:
                return
            
            #reciursive case
            cur_left = left_node
            cur_right = right_node

            left_node = left_node.next
            right_node = prev_map[right_node]
            right_node.next = None

            cur_left.next = cur_right
            cur_right.next = left_node

            return rearrange(left_node, right_node, prev_map)

        rearrange(left, right, prev_map)
       

        
