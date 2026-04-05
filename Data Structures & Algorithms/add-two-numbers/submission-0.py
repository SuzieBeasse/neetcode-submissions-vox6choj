# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        head = ListNode()
        curr_node = head
        ret = 0

        while l1 or l2 or ret>0:
            cur1 = l1.val if l1 else 0
            cur2 = l2.val if l2 else 0
            ret, curr_val = divmod(ret + cur1 + cur2, 10)
            curr_node.val = curr_val
            if (l1 and l1.next) or (l2 and l2.next) or ret>0:
                curr_node.next = ListNode()
                curr_node = curr_node.next
                l1 = l1.next if l1 else None
                l2 = l2.next if l2 else None
            else:
                break
        return head

            
