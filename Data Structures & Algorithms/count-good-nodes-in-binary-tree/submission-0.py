# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = 1
        def dfs(node:TreeNode, curr_max: int): 
            if not node:
                return 0
            ans = 1 if node.val >= curr_max else 0
            curr_max = max(node.val, curr_max)

            ans += dfs(node.left, curr_max)
            ans += dfs(node.right, curr_max)

            return ans
        
        return dfs(root, root.val)
        
        
        
        

       
        