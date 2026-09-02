# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.dfs(root, p, q)
        return lca
    
    def dfs(self, node: TreeNode, p: TreeNode, q: TreeNode):
        global lca
        if not node:
            return False
        
        node_p_or_q = node == p or node == q

        right_p_or_q = self.dfs(node.right, p, q)
        left_p_or_q = self.dfs(node.left, p, q)
        if (right_p_or_q + left_p_or_q + node_p_or_q) == 2:
            lca = node
        return node_p_or_q or right_p_or_q or left_p_or_q


        