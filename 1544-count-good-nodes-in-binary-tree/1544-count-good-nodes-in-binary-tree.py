# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        queue = deque()

        cp = 0
        queue.append((root, root.val))

        # stack 
        # recursive

        def dfs(node, curr_max):
            nonlocal cp
            if node == None:
                return
            if curr_max <= node.val:
                cp +=1
            
            dfs(node.left, max(curr_max, node.val))
            dfs(node.right, max(curr_max, node.val))
        
        dfs(root, root.val)
        return cp
        # while queue:
        #     node, curr_max = queue.popleft()
        #     if node == None:
        #         continue
        #     if curr_max <= node.val:
        #         cp +=1
            
        #     queue.append((node.left, max(curr_max, node.val)))
        #     queue.append((node.right, max(curr_max, node.val)))
        
        # return cp
        