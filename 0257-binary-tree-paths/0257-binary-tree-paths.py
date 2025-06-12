# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        bucket = list()
        def backtracking(node, path):
            if node == None:
                return
            if node.left == None and node.right == None:
                # we add the path to our bucket
                path.append(str(node.val))
                bucket.append(path)
                return
            
            path.append(str(node.val))
            backtracking(node.left, path.copy())
            # path.pop()
            backtracking(node.right, path.copy())

        backtracking(root, [])
        # print(bucket)

        ans = []
        for val in bucket:
            tmp = "->".join(val)
            ans.append(tmp)
        
        return (ans)

