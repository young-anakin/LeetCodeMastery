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

        arr = []
        #left = True
        xx = root
        def bfs(parent, node, ind, flag):
            if node == None:
                return
            
            # print(node.val)



            if ind == 0:
                pass
            elif flag:
                # print("hiiii", node.val)
                node.next = parent.right
                # print(node.next.val)
            else:
                # print("byeeee", node.val)
                if parent.next == None:
                    node.next = None
                else:
                    node.next = parent.next.left
                    # print("hiiii", node.val)
                    # print(node.next.val)
            
            bfs(node, node.left, ind+1, True)
            bfs(node, node.right, ind+1, False)

        def dfs(parent, node, ind, flag):
                    if node == None:
                        return
                    
                    # print(node.val)

                    bfs(node, node.left, ind+1, True)
                    bfs(node, node.right, ind+1, False)

                    if ind == 0:
                        pass
                    elif flag:
                        print("hiiii", node.val)
                        # node.next = parent.right
                        # print(node.next.val)
                    else:
                        # print("byeeee", node.val)
                        if parent.next == None:
                            node.next = None
                        else:
                            node.next = parent.next.left
                            # print("hiiii", node.val)
                            # print(node.next.val)

        


        
        bfs(None, xx, 0, False)
        # dfs(None, xx, 0, False)


        return xx


            



            
        