# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        ss = set()
        queue = deque()

        
        queue.append(root)

        while queue:
            curr = queue.popleft()
            if curr != None:
                ss.add(curr.val)
                queue.append(curr.left)
                queue.append(curr.right)
        


        # dfs(root)
        return len(ss) == 1