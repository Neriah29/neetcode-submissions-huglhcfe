# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        [1,2,4], 
        [1,3,5]
        [1, ]
        """
        res_list = ListNode()
        res_pointer = res_list

        cur_list1_node, cur_list2_node = list1, list2

        while cur_list1_node and cur_list2_node:
            list1_val = cur_list1_node.val
            list2_val = cur_list2_node.val

            if  list1_val < list2_val:
                res_pointer.next = ListNode(list1_val)
                cur_list1_node = cur_list1_node.next
            else:
                res_pointer.next = ListNode(list2_val)
                cur_list2_node = cur_list2_node.next
            
            res_pointer = res_pointer.next
        
        if cur_list1_node:
            res_pointer.next = cur_list1_node
        if cur_list2_node:
            res_pointer.next = cur_list2_node
        
        return res_list.next

                

