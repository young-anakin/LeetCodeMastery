# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        if k == 0:
            return head
        curr = head
        cp = 0
        while curr.next:
            cp +=1
            curr = curr.next
        cp +=1
        k %= cp
        curr.next = head
        # print(cp,k)
        ind = 0
        curr = head
        ans = ListNode(10)
        fin = ans
        # print(curr)
        while ind < cp-k:
            curr = curr.next
            # print("ua0", curr.val)

            ind +=1
        # print(curr.val)
        for ind in range(cp):
            # print(curr.val)

            tmp = ListNode(curr.val)
            curr = curr.next
            ans.next = tmp
            ans = ans.next
        fin = fin.next
        return fin
        # curr.next = head
