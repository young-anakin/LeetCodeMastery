# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1 = []
        leaf2 = []


        def dfs(node, arr):
            if node == None:
                return

            if node.left == None and node.right == None:
                arr.append(node.val)
            
            dfs(node.left, arr)

            dfs(node.right, arr)


            return arr


        leaf1 = dfs(root1, [])
        leaf2 = dfs(root2, [])

        print(leaf1, leaf2)

        if len(leaf1) != len(leaf2):
            return False
        for ind in range(len(leaf1)):
            if leaf1[ind] != leaf2[ind]:
                return False
        
        return True
        
        