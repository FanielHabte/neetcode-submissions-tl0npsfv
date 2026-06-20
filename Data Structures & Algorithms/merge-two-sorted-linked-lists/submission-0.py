# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode(0)
        tail = head

        # loop if both lists are not None
        while list1 and list2:

            # check if list1 value is greater
            if list1.val < list2.val:
                # point my tail to list1
                tail.next = list1
                # move list1 and tail forward
                list1 = list1.next
                tail = tail.next
            else:
                # point tail to list2
                tail.next = list2
                # move list2 and tail forward
                list2 = list2.next
                tail = tail.next
        
        # check left over fragments of list1 or list2 
        # and point tail to the left list node give everything is sorted
        # one list node should be None give we are moving the node forward in the loop above
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        # return node excluding the head(dummy) node
        return head.next

            

