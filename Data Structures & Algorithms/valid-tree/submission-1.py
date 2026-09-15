from collections import defaultdict, deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        seen = set()
        center = 0
        hm = defaultdict(list)
        for a, b in edges:
            hm[a].append(b)
            hm[b].append(a)
            if len(hm[a]) > len(hm[center]):
                center = a
            if len(hm[b]) > len(hm[center]):
                center = b
            
        
        def dfs(node, parent):
            if len(hm[node]) == 1:
                return True
            ans = True
            for neigh in hm[node]:        
                if neigh != parent:
                    if neigh in seen:
                        return False
                    seen.add(neigh)
                    ans = ans and dfs(neigh, node)
            return ans

        seen.add(center)
        
        a = dfs(center, -1)
        return a and len(seen) == n


        