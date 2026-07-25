# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        even, odd = head, head
        while even and odd and even.next:
            even = even.next.next
            odd = odd.next
            if even == odd:
                return True
            
            
        return False
        