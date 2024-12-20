# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        cp = 0
        dd = defaultdict(list)
        def bfs(node, ind):
            if node == None:
                return
            dd[ind].append(node.val)
            bfs(node.left, ind+1)
            bfs(node.right, ind+1)
        bfs(root, 0)
        
        for key, val in dd.items():
            if key %2 != 0:
                pass
                # dd[key] = val[::-1]
        ans = TreeNode(dd[0][0])

        # for key, items in dd.items():
        #     if key%2 == 0:

        def bfs(node, ind):
            if node == None:
                return

            if ind % 2 != 0:
                node.val = dd[ind].pop()

            bfs(node.left, ind+1)
            bfs(node.right, ind+1)
            
        
        bfs(root, 0)
        # print(dd)

        return root