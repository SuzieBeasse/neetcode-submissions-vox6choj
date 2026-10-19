"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def __init__(self):
        self.hm = dict()
    
    def dfs(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
                return

        if node.val in self.hm:
            return self.hm[node.val]
            
        cloned = Node(node.val)
        self.hm[node.val] = cloned
        neighb = []
        
        for neigh in node.neighbors:
            c_neigh = self.dfs(neigh)
            neighb.append(c_neigh)


        self.hm[node.val].neighbors = neighb
        return self.hm[node.val]

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return  
        return self.dfs(node)
        
    


        