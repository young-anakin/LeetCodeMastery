"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        # bfs for level order traversal
        
        deck = deque([root])
        answer = []
        
        while deck:
            temp = []
            for i in range(len(deck)):
                node = deck.popleft()
                temp.append(node.val)
                deck.extend(node.children)
            answer.append(temp)
            
        return answer