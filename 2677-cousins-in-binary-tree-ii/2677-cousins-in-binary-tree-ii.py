# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        depth = defaultdict(int)


        def dfs(node, d):
            if node == None:
                return

            
            depth[d] += node.val
            dfs(node.left, d+1)
            dfs(node.right, d+1)

        
        def calc(node, d):
            if node == None:
                return

            sm_r, sm_l = 0,0
            if node.right:
                sm_r = node.right.val
            if node.left:
                sm_l = node.left.val

            sm = sm_r + sm_l
            if node.left:

                node.left.val = depth[d+1] - sm
                # print(sm)
                calc(node.left, d+1)

            if node.right:
                node.right.val = depth[d+1] - sm
                # print("right", node.val, sm, depth[d+1])
                calc(node.right, d+1)

            
        dfs(root, 0)
        root.val = 0

        calc(root, 0)

        print(depth)
        return(root)