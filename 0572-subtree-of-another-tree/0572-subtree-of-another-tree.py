# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        def bfs(a, b):
            # print("steve", a, b)
            if a == None:
                # print("roll")
                if b == None:
                    return True
                else:
                    return False
            
            if b == None:
                if a == None:
                    return True
                else:
                    return False
            
            if a:
                if b:
                    if a.val == b.val:
                        # print("kazakaaaaa")
                        return bfs(a.left, b.left) and bfs(a.right, b.right)
                        

                else:
                    # print("yo")
                    return False
            
            else:
                return False

            return False
            
            
            # if a.val == b.val

            
        fl = False
        def dfs(root):
            nonlocal fl
            if root == None:
                return

            
            # print(root, subRoot)
            if root.val == subRoot.val:
                # print(root, subRoot, root == subRoot)
                if fl == False:
                    fl = bfs(root, subRoot)
                # print(fl)

            dfs(root.right)
            dfs(root.left)

        dfs(root)
        

        return fl
            
