from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 1:
            return [0]
        adj = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses
        ans = []

        for a, b in prerequisites:
            adj[b].append(a)
            indegrees[a] += 1

        queue = deque([])

        # Look for the courses that don't need any prerequisite
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)


        while queue:
            i = queue.popleft()
            ans.append(i)
            for neigh in adj[i]:
                indegrees[neigh] -= 1
                if indegrees[neigh] == 0:
                    queue.append(neigh)
        
        if len(ans) != numCourses:
            return []
        print(ans)
        return ans

