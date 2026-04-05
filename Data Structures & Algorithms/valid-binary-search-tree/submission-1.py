# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left = self.dfs(root.left, root.val, float('-inf'))
        right = self.dfs(root.right, float('inf'), root.val)
        return right and left


    def dfs(self, node: Optional[TreeNode], curr_max, curr_min) -> bool:
        if not node:
            return True
        if node.val <= curr_min or node.val >= curr_max:
            return False
        right = self.dfs(node.right, curr_max, node.val)
        left = self.dfs(node.left, node.val, curr_min)

        return right and left

        