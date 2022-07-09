# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr = head

        while curr:
            if head.val == val:
                head = curr.next
                curr = head
            else:
                ref = curr.next

                if ref and ref.val == val:
                    curr.next = ref.next
                    ref.next = None
                else:
                    curr = curr.next

        return head