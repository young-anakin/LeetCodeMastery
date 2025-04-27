# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        pre = []
        def preorder(root):
            if not root:
                return
            
            pre.append(root.val)
            preorder(root.left)
            preorder(root.right)
        
        preorder(root)
        i = 0
        def dfs(root, i):
            if i >= len(pre):
                return
            # nonlocal i
            # print(root.val)
            node = TreeNode(pre[i])
            # print(node)
            root.right = node
            root.left = None
            # root.val = pre[i]
            # i +=1
            dfs(root.right, i+1)
        dfs(root, 1)
        if root:
            root = root.left
            # print(root.right)
            # print(root.left)
        # return root
            