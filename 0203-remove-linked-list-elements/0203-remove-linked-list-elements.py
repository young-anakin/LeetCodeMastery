# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = ListNode(0)
        curr = head
        ans = ListNode(0)
        ret = ans
        while curr:
            if curr.val == val:
                curr = curr.next
            else:
                tt = ListNode(curr.val)
                ans.next = tt
                ans = ans.next
                curr = curr.next
        
        ret = ret.next
        return ret


        # while curr:
        #     if curr.val == val:
        #         if curr.next:
        #             prev.next = curr.next
        #             curr = curr.next

        #         else:
        #             prev.next = None
        #             curr = None
            
        #     else:
        #         prev = curr
        #         curr = curr.next
            
        #     # print(curr.val)
        
        # hh = hh.next
        # return head