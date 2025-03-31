# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(node):
            prev = None
            curr = node
            next = curr.next

            while next:
                curr.next = prev
                prev = curr
                curr = next
                next = curr.next
                # curr = curr.next
            curr.next = prev

            return curr
        
        l1 = reverse(l1)
        l2 = reverse(l2)
        ans = ListNode()
        dummy = ans
        overtake = 0
        # print(l1)
        # print(l2)
        summand = 0
        while l1 and l2:
            summand = (l1.val + l2.val + overtake)
            if summand >= 10:
                summand = str(summand)[1]
                overtake = 1
            else:
                summand = str(summand)[0]
                overtake = 0
            tmp = ListNode(int(summand))
            # print(tmp)
            dummy.next = tmp
            dummy = dummy.next
            l1 = l1.next
            l2 = l2.next
        ans = ans.next

        print(ans, overtake, l2)
        while l1:
            if l1.val + overtake >= 10:
                tmp = ListNode(0)
                overtake = 1
            else:
                tmp = ListNode(l1.val + overtake) 
                overtake = 0
            dummy.next = tmp
            dummy = dummy.next
            l1 = l1.next
        while l2:
            if l2.val + overtake >= 10:
                tmp = ListNode(0)
                overtake = 1
            else:
                tmp = ListNode(l2.val + overtake)
            # print("Temp", tmp)

                overtake = 0
            dummy.next = tmp
            dummy = dummy.next
            l2 = l2.next
        
        if overtake > 0:
            dummy.next = ListNode(1)
        ans = reverse(ans)
        return ans
        print(ans)

