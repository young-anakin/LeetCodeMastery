# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        if not p or not q:
            return False
        # if not p and not q:
        #     return False
        
        def dfs(p, q):

            if p == None and q == None:
                return True
            elif (p == None and q!= None) or (p != None and q == None):
                return False
            if p.val != q.val:
                return False
            

            return dfs(p.right, q.right) and dfs(p.left, q.left)
        
        return dfs(p, q)


            