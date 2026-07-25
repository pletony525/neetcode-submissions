# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2
        result = ListNode()
        temp = result
        while cur1 or cur2:
            if cur1 and not cur2:
                temp.next = cur1
                cur1 = cur1.next
                temp = temp.next
            elif cur2 and not cur1:
                temp.next = cur2
                cur2 = cur2.next
                temp = temp.next
            else:
                if cur1.val <= cur2.val:
                    temp.next = cur1
                    cur1 = cur1.next
                    temp = temp.next
                elif cur2.val <= cur1.val:
                    temp.next = cur2
                    cur2 = cur2.next
                    temp = temp.next
        return result.next
            
                

