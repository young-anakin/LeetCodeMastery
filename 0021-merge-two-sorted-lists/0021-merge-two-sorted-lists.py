# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        ans = ListNode()
        fin = ans
        while list1 and list2:
            if list1.val < list2.val:
                nn = ListNode(list1.val)
                ans.next = nn
                ans = ans.next
                list1 = list1.next
            else:
                nn = ListNode(list2.val)
                ans.next = nn
                ans = ans.next
                list2 = list2.next
        
        while list1:
            nn = ListNode(list1.val)
            ans.next = nn
            ans = ans.next
            list1 = list1.next
        while list2:
            nn = ListNode(list2.val)
            ans.next = nn
            ans = ans.next
            list2 = list2.next
        return fin.next
            
