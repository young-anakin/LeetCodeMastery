# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        

        parents = defaultdict(int)

        parents2 = defaultdict(int)

        def dfs(node, parents):
            if node == None:
                return 
            

            
            if node.right != None:
                parents[node.right.val] = node.val
            
            if node.left != None:
                parents[node.left.val] = node.val
            
            dfs(node.left, parents)

            dfs(node.right, parents)


        dfs(root1, parents)
        dfs(root2, parents2)

        if root1:
            parents[root1.val] = -1
        
        if root2:
            parents2[root2.val] = -1

        
        return parents == parents2
