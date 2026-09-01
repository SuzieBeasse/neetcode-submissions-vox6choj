# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []

        def dfs(node, values):
            if not node:
                return
            if not node.right and not node.left:
                values.append(node.val)
                return
            dfs(node.left, values)
            values.append(node.val)
            dfs(node.right, values)
        
        dfs(root, values)

        return values[k-1]
        


        