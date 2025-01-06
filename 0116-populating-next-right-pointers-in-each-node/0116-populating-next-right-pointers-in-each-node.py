"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def bfs(parent, node, ind, flag):
            if node == None:
                return
            if ind == 0:
                pass
            elif flag:
                node.next = parent.right
            else:
                if parent.next == None:
                    node.next = None
                else:
                    node.next = parent.next.left
            
            bfs(node, node.left, ind+1, True)
            bfs(node, node.right, ind+1, False)

        bfs(None, root, 0, False)


        return root


            



            
        