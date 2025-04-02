# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        fl = True
        def bfs(node):
            nonlocal fl
            # if node == None:
            #     return 
            if node.left == None and node.right == None:
                return (node.val, node.val)
            

            if node.left and node.right:
                x = bfs(node.left)
                y = bfs(node.right)
                if (node.val <= x[0] or node.val <= x[1]):
                    fl = False
                
                if (node.val >= y[0] or node.val >= y[1]):
                    fl = False
                return (min(x[0], x[1], y[0], y[1]), max(x[0], x[1], y[0], y[1]))

                # pass
            elif node.left and not node.right:
                y = bfs(node.left)

                if (node.val <= y[0] or node.val <= y[1]):
                    fl = False
                return (min(node.val, y[0]), max(node.val, y[1]))
            elif node.right and not node.left:
                y = bfs(node.right)

                if (node.val >= y[0] or node.val >= y[1]):
                    fl = False
                return (min(node.val, y[0]), max(node.val, y[1]))
            



        bfs(root)
        return (fl)
