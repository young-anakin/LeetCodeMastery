from collections import deque

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        # Step 1: Store nodes in a deque
        node_deque = deque()
        tmp = head
        while tmp:
            node_deque.append(tmp)  # Store the actual node, not the value
            tmp = tmp.next
        
        # Step 2: Reconstruct the list by alternating from front and back
        while len(node_deque) > 1:
            front = node_deque.popleft()
            back = node_deque.pop()
            
            # Reorder pointers
            front.next = back
            if len(node_deque) > 0:
                back.next = node_deque[0]  # Point back to the next front node
        
        # Step 3: Terminate the list
        if node_deque:  # If one node is left, terminate it
            node_deque[0].next = None
        else:
            back.next = None
