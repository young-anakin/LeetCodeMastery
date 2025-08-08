# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        # DFS 

        sm = 0

        queue = deque()
        
        queue.append((root, False))

        while queue:
            node, check = queue.popleft()
            if node == None:
                continue
            if check == True and node.left == None and node.right == None:
                sm += node.val

            queue.append((node.left, True))
            queue.append((node.right, False))



        return sm
