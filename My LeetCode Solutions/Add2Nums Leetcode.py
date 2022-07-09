# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        num1, num2 = 0, 0
        mult1, mult2 = 1, 1
        ans_list = []

        # first number as num1
        while True:
            num1 += curr1.val * mult1
            curr1 = curr1.next
            mult1 *= 10
            if not curr1:
                break

        # second number as num2
        while True:
            num2 += curr2.val * mult2
            curr2 = curr2.next
            mult2 *= 10
            if not curr2:
                break

        sum = num1 + num2

        if sum == 0:
            ans_list.append(sum)
        else:
            while sum:
                dig = sum % 10
                ans_list.append(dig)
                sum = sum // 10

        inst = None
        for obj in ans_list[::-1]:
            value = obj
            inst = ListNode(value, inst)

        return inst