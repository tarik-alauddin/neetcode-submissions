# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def recurse(self, head: Optional[ListNode], n: [int]) -> Optional[ListNode]:
        if not head:
            return

        print(head.val, n)
        
        # traverse forward until end
        head.next = self.recurse(head.next, n)

        print(head.val, n)

        n[0] = n[0] - 1
        if n[0] == 0:
            # at Nth node from end, so return node ahead
            return head.next

        return head


    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        return self.recurse(head, [n])