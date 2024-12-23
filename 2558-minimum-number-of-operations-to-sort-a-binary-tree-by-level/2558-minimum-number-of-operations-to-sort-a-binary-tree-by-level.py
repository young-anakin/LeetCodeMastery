# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        dd = defaultdict(list)
        def bfs(root, level):
            if root == None:
                return
            dd[level].append(root.val)

            bfs(root.left, level+1)
            bfs(root.right, level+1)


        def getSwaps(arr):
            # Step 1: Copy the input array and sort it
            sorted_arr = sorted(arr)

            # Step 2: Create a mapping of each element to its index
            index_map = {value: index for index, value in enumerate(arr)}

            # Step 3: Initialize variables
            swaps = 0
            for i in range(len(arr)):
                # Check if the current element is in the correct position
                if arr[i] != sorted_arr[i]:
                    # Find the correct position of the current element
                    correct_value = sorted_arr[i]
                    correct_index = index_map[correct_value]

                    # Swap the current element with the correct element
                    arr[i], arr[correct_index] = arr[correct_index], arr[i]

                    # Update the mapping
                    index_map[arr[correct_index]] = correct_index
                    index_map[arr[i]] = i

                    # Increment the swap count
                    swaps += 1

            return swaps
        

        bfs(root, 0)
        cp = 0
        # print(dd)
        tot = 0
        for ind, val in dd.items():
            print(val)
            cp += getSwaps(val)


        print(cp)
        return cp
        
