# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # The last value and 
        # if index > 0 then there is a cycle
        dict_node = dict()
        curr = head
        while curr:
            if curr in dict_node:
                return True
                
            dict_node[curr] = curr.val
            curr = curr.next
        return False