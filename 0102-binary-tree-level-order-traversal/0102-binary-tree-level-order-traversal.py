# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans = defaultdict(list)
        queue = deque()
        queue.append((root, 0))
        while queue:
            node, level = queue.popleft()
            if node == None:
                continue
            ans[level].append(node.val)
            queue.append((node.left, level+1))
            queue.append((node.right, level+1))
        
        fin = list()
        for key, val in ans.items():
            fin.append(val)
        
        return fin