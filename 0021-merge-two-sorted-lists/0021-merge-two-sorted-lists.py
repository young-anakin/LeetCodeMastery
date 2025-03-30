# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        ans = ListNode()
        dummy = ans

        while list1 and list2:
            if list1.val < list2.val:
                tmp = ListNode(list1.val)
                dummy.next = tmp
                dummy = dummy.next
                list1 = list1.next
            else:
                tmp = ListNode(list2.val)
                dummy.next = tmp
                dummy = dummy.next
                list2 = list2.next
        
        while list1:
            tmp = ListNode(list1.val)
            dummy.next = tmp
            dummy = dummy.next
            list1 = list1.next
        while list2:
            tmp = ListNode(list2.val)
            dummy.next = tmp
            dummy = dummy.next
            list2 = list2.next
        
        ans = ans.next
        return ans
