# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        head = ans

        def reverse(node):
            prev = None
            curr = node
            next = None
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            
            return prev
        
        # l1 = reverse(l1)
        # l2 = reverse(l2)
        carry = 0
        while l1 and l2:
            tmp = l1.val + l2.val + carry
            if tmp >= 10:
                head.next = ListNode((( tmp)%10))
                carry = 1
            else:
                head.next = ListNode( tmp)
                carry = 0
            head = head.next

            l1 = l1.next
            l2 = l2.next
        print(carry)
        while l1:
            tmp = (carry + l1.val)
            if tmp >= 10:
                head.next = ListNode(((tmp)%10))
                carry = 1
            else:
                head.next = ListNode(tmp)
                carry = 0
            head = head.next
            l1 = l1.next
            # l2 = l2.next
        while l2:
            tmp = (carry + l2.val)
            if tmp >= 10:
                head.next = ListNode((( tmp)%10))
                carry = 1
            else:
                head.next = ListNode(tmp)
                carry = 0
            head = head.next
            # l1 = l1.next
            l2 = l2.next
        
        if carry == 1:
            head.next = ListNode(1)
        ans = ans.next
        return (ans)







        
            