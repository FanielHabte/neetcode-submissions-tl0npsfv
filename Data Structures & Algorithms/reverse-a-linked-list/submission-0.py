# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            # Initial: 0 -> 1 -> 2
            # After Assignment: None(prev) -> 0(cur) -> 1(next) -> 2
            # Final:  None <- 0(prev) 1(curr) -> 2

            # 1. save the next node in temp variable
            # 2. filp the pointer by pointing next to prev
            # 3. move curr forward by setting it to next
            # 4. move prev forward by setting it to cur

            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev




